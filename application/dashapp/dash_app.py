"""Create a Dash app within a Flask app."""

from dash import Dash
from dash.dependencies import Input, Output

from .layout_content import layout


def Add_Dash(server):
    """Create a Dash app."""
    external_stylesheets = ['/static/src/css/base.css',
                            '/static/src/css/styles.css',
                            'https://fonts.googleapis.com/css?family=Lato',
                            'https://use.fontawesome.com/releases/v5.8.1/css/all.css']
    external_scripts = ['/static/dist/js/includes/jquery.min.js',
                        '/static/dist/js/main.js']
    dash_app = Dash(server=server,
                    external_stylesheets=external_stylesheets,
                    external_scripts=external_scripts,
                    routes_pathname_prefix='/dashapp/')


    # Create Dash Layout
    dash_app.layout = layout

    # Initialize callbacks after our app is loaded
    # Pass dash_app as a parameter
    init_callbacks(dash_app)

    return dash_app.server


def init_callbacks(dash_app):
    @app.callback(
        # ... Callback input/output
        )
    def update_graph():
        # ... Insert callback stuff here
