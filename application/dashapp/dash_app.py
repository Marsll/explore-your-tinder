"""Create a Dash app within a Flask app."""

import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output

from .alt_index_string import html_layout
from .layout_content import get_layout


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

    # Create Dash Layout comprised of Data Tables
    dash_app.layout = html.Div([dcc.Location(id='url', refresh=True),
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
        from .process_input import get_data

        data = get_data("application/static/uploads/data.json")
        return get_layout(data)
