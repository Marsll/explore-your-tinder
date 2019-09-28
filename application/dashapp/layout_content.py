import dash_core_components as dcc
import dash_html_components as html
from .process_input import get_data

data = get_data("application/static/data/data.json")
layout = html.Div(
        [
            html.Div(
                [html.H6(data["match_rate"]), html.P("Matchrate")],
                id="wells",
                className="mini_container",
            ),
            html.Div(
                [html.H6(id="gasText"), html.P("Gas")],
                id="gas",
                className="mini_container",
            ),
            html.Div(
                [html.H6("100"), html.P("Oil")],
                id="oil",
                className="mini_container",
            ),
            html.Div(
                [html.H6(id="waterText"), html.P("Water")],
                id="water",
                className="mini_container",
            ),
        ],
        id="info-container",
        className="row container-display",
)