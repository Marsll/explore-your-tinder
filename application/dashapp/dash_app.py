"""Create a Dash app within a Flask app."""

import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
from flask import current_app as app
import logging

from .alt_index_string import html_layout
from .layout_content import get_layout
from .main_graph import create_sankey, get_dicts, get_dicts_zoom
from .process_input import get_data


def add_dash(server):
    """Create a Dash app."""
    external_stylesheets = ['/static/src/css/styles.css',
                            "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/dist/js/includes/jquery.min.js',
                        '/static/dist/js/main.js']
    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    external_scripts=external_scripts,
                    routes_pathname_prefix='/dashapp/')

    # Override the underlying HTML template
    dash_app.index_string = html_layout
    dash_app.config.suppress_callback_exceptions = True
    # Create Dash Layout comprised of Data Tables
    dash_app.layout = html.Div([dcc.Location(id='url', refresh=False),
                                html.Div(id='layout_injector')]
                               )
    init_callback(dash_app)
    return dash_app.server


def init_callback(dash_app):
    from application import db
    from application.models import User
    
    @dash_app.callback(Output('layout_injector', 'children'),
                       [Input('url', 'pathname')])
    def load_data(pathname):
        # Super weird behavior, first NoneType, then class str...
        # print(type(pathname), pathname)
        from .process_input import get_data
        if pathname is not None:
            if pathname.startswith('/dashapp/'):
                pathname = pathname.replace('/dashapp/', '')
                try:
                    data = get_data(
                        "application/static/uploads/" + pathname + ".json")
                    return get_layout(data)
                except:
                    return html.Div(
                        "Sorry, but you tried to access a non-existent url",
                         className="container")

    @dash_app.callback(
        Output(component_id='sankey-graph', component_property='figure'),
        [Input(component_id='button', component_property='n_clicks'), 
        Input(component_id='toggle-zoom', component_property='value')],
        [State('numbers', 'value'),
        State('dates', 'value'),
        State('hookups', 'value'),
        State('f+s', 'value'),
        State('relationships', 'value'),
        State('nothing', 'value')]#,
        #State('toggle-zoom', 'value')]
    )
    def update_output(n_clicks, zoom, numbers, dates, hookups, fplus, relationships, nothing):
        if n_clicks is None:# and zoom is False:
            raise PreventUpdate
        else: 
            # TODO add other to data and test (already implemented)
            data = get_data("application/static/uploads/data.json")
            data["numbers"] = numbers
            data["dates"] = dates
            if zoom:
                node_dict, link_dict = get_dicts_zoom(data)
            else:
                node_dict, link_dict = get_dicts(data)
            return go.Figure(data=[create_sankey(node_dict, link_dict)])

    @dash_app.callback(
        Output(component_id='button', component_property='n_clicks'),
        [Input(component_id='toggle-zoom', component_property='value')],
        [State(component_id='button', component_property='n_clicks')]
        )
    # Set n_clicks to 1 to be able to use toggle before submit 
    def update_output(zoom, n_clicks):
        if zoom is False and n_clicks is None:
            raise PreventUpdate
        else: 
            return 1
