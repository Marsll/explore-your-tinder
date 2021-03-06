import math as m

import dash_core_components as dcc
import dash_html_components as html


def generate_card(description, value, icon, id=None):
    card =  html.Div(
                [html.Div(
                    [html.Div(
                        [html.Div(
                            [
        html.H6(description, className="card-title text-uppercase text-muted mb-2"),
        html.Span(value, className="h2 mb-0"),
                            ],
                        className="col"),
                        html.Div(
                            [
                                html.I(className=icon)
                            ],
                        className="col-auto")
                        ],
                    className="row align-items-center")
                    ],
                className="card-body")
                ], 
            className="card border-secondary"                
            )
    return card


# card component
def four_cards(data):
    four_cards = html.Div(
        [html.Div(
            # Card 1
            [generate_card(
                    "Matchrate",
                    f"{m.ceil(data['match_rate']):d}%",
                    icon="fas fa-fire")
            ],
        className="col-12 col-lg-6 col-xl"),

        html.Div(
            # Card 2
            [generate_card(
                    "Swipes",
                    data['swipes_total'],
                    icon="far fa-hand-point-up" )
            ],
        className="col-12 col-lg-6 col-xl"),

        html.Div(
            # Card 3
            [generate_card(
                    "Ranking",
                    data['ranking'],
                    icon="fas fa-trophy")
            ],
        className="col-12 col-lg-6 col-xl"),

        html.Div(
            # Card 4
            [generate_card(
                    "Usage time",
                    data['usage_time'],
                    icon="far fa-calendar-alt")
            ],
        className="col-12 col-lg-6 col-xl")

        ], 
    className="row mb-2"
    )          

    return four_cards


def card_container(headline=None, children=None):

    if headline is not None:
        card_container = html.Div(
            [html.Div(
                [html.H5(headline, className="")],
            className="card-header text-white bg-pink"),

            html.Div(children=children, className="card-body")
            ],
        className="card mb-2 border-secondary"    
        )
    else:
        card_container = html.Div(
            [html.Div(children=children, className="card-body")],
            className="card mb-2 border-secondary")

    return card_container
