import dash_core_components as dcc
import dash_html_components as html

from .cards import four_cards
from .main_graph import sankey_graph, double_sankey
from .tabs import tabs


def get_layout(data):
    layout = html.Div([html.Div(

        [html.Div(html.H1("Your RESULTS"), ),
            html.Div(
        [
            html.Div(
                [html.H6(f"{data['match_rate']:d}%"), html.P("Matchrate")],
                id="wells",
                className="mini_container",
            ),
            html.Div(
                [html.H6(data['swipes_total']), html.P(
                    "Total number of swipes")],
                id="gas",
                className="mini_container",
            ),
            html.Div(
                [html.H6("100"), html.P("Ranking")],
                id="oil",
                className="mini_container",
            ),
            html.Div(
                [html.H6(data['usage_time']), html.P("Usage time")],
                id="water",
                className="mini_container",
            ),
        ],
        id="info-container",
        className="row container-display",
    ),
        html.Div([sankey_graph(data)]
                 ),
        html.Div([tabs(data)]),
        #html.Div([double_sankey(data)]),
    ], className="container",
    )
])
    return layout
