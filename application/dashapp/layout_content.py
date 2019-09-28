import dash_core_components as dcc
import dash_html_components as html

from .main_graph import m_graph


def get_layout(data):
    layout = html.Div([html.Div(
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
        html.Div([m_graph]
                 )
    ]
    )

    return layout
