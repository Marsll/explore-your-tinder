import dash_core_components as dcc
import dash_html_components as html

from .cards import card_container, four_cards
from .main_graph import double_sankey, sankey_graph
from .tabs import tabs


def get_layout(data):
    layout = html.Div(
        [html.Div(
            [html.Div(html.H1("Your RESULTS"), id="h1-results"),

            html.Div([four_cards(data)], id="four_cards"),

            card_container("Sankey diagram", [sankey_graph(data)]),

            card_container("Development over time", [tabs(data)]),
            ], 
        className="container")
        ],
        id = "main-dash-app",
        className="bg-light"
)
    return layout
