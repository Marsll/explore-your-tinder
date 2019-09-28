import dash_core_components as dcc
import dash_html_components as html

from .process_input import get_data

<<<<<<< HEAD
data = get_data("application/static/data/data.json")
layout = html.Div(
        [
            html.Div(
                [html.H6(f"{data['match_rate']:d}%"), html.P("Matchrate")],
                id="matchrate",
                className="mini_container",
            ),
            html.Div(
                [html.H6(data['swipes_total']), html.P("Total number of swipes")],
                id="swipes_total",
                className="mini_container",
            ),
            html.Div(
                [html.H6("100"), html.P("Ranking")],
                id="ranking",
                className="mini_container",
            ),
            html.Div(
                [html.H6(data['usage_time']), html.P("Usage time")],
                id="usage_time",
                className="mini_container",
            ),
        ],
        className="row container-display",
)
=======
# data = get_data("application/static/uploads/data.json")


def get_layout(data):
    layout = html.Div(
            [
                html.Div(
                    [html.H6(f"{data['match_rate']:d}%"), html.P("Matchrate")],
                    id="wells",
                    className="mini_container",
                ),
                html.Div(
                    [html.H6(data['swipes_total']), html.P("Total number of swipes")],
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
    )
    return layout
>>>>>>> 59c6b38171660dcce2755ff212799b2f920f909a
