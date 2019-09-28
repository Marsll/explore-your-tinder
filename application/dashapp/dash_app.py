"""Create a Dash app within a Flask app."""

from .layout_content import layout
from dash import Dash


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
    dash_app.layout = layout

    return dash_app.server
