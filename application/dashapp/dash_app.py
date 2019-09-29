"""Create a Dash app within a Flask app."""

import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output

from .alt_index_string import html_layout
from .cards import card_container
from .layout_content import get_layout


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

    # The main hack to inject the layout after file was processed
    dash_app.layout = html.Div([dcc.Location(id='url', refresh=False),
                          html.Div([
                                # Plot Layout
                                html.Div(id='layout_injector'),
                                # New card with switch
                          ], className="container")      
                            
    ], id = "main-dash-app",
        className="bg-light"
    )
    init_callback(dash_app)
    return dash_app.server


def init_callback(dash_app):
    @dash_app.callback(Output('layout_injector', 'children'),
                       [Input('url', 'pathname')])
    def load_data(pathname):
        from .process_input import get_data

        data = get_data("application/static/uploads/data.json")
        return get_layout(data)


    @dash_app.callback(
        Output('toggle-switch-output', 'children'),
        [Input('my-toggle-switch', 'value')])
    def update_output(value):
        return 'The switch is {}.'.format(value)

    @dash_app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value')])
    def update_output(n_clicks, input1, input2):
        return ('The Button has been pressed {} times,'
            'Input 1 is "{}",'
            'and Input 2 is "{}"').format(n_clicks, input1, input2)
