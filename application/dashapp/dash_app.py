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
from .main_graph import create_sankey, get_dicts
from .process_input import get_data

def Add_Dash(server):
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
    dash_app.layout = html.Div([dcc.Location(id='url', refresh=True),
                                html.Div(id='layout_injector')]
                               )
    init_callback(dash_app)
    return dash_app.server


def init_callback(dash_app):
    @dash_app.callback(Output('layout_injector', 'children'),
                       [Input('url', 'pathname')])
    def load_data(pathname):


        data = get_data("application/static/uploads/data.json")
        return get_layout(data)

    @dash_app.callback(
        Output(component_id='sankey-graph', component_property='figure'),
        [Input(component_id='button', component_property='n_clicks')],
        [State('numbers', 'value'),
        State('dates', 'value'),
        State('hookups', 'value'),
        State('f+s', 'value'),
        State('relationships', 'value'),
        State('nothing', 'value'),
        State('toggle-zoom', 'value')]
    )
    def update_output(n_clicks, numbers, dates, hookups, fplus, relationships, nothing, zoom):
        if n_clicks is None:
            raise PreventUpdate
        else: 
            data = get_data("application/static/uploads/data.json")
            data["numbers"] = numbers
            data["dates"] = dates
            node_dict, link_dict = get_dicts(data)
            return go.Figure(data=[create_sankey(node_dict, link_dict)])