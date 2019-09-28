"""Create a Dash app within a Flask app."""

import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output

from .layout_content import get_layout


def Add_Dash(server):
    """Create a Dash app."""
    external_stylesheets = ['/static/src/css/styles.css',
                            '/static/src/css/s1.css',
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/dist/js/includes/jquery.min.js',
                        '/static/dist/js/main.js']
    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    external_scripts=external_scripts,
                    routes_pathname_prefix='/dashapp/')

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
        from .process_input import get_data

        data = get_data("application/static/uploads/data.json")
        return get_layout(data)
