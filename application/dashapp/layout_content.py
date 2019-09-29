import dash_core_components as dcc
import dash_html_components as html

from .cards import card_container, four_cards
from .main_graph import double_sankey, sankey_graph
from .tabs import tabs


def get_layout(data):
    layout = html.Div(
        [html.Div(
            [card_container(children=[
                dcc.Markdown('''
#### These are **your results**.

To share them with friends, generate [your personal link](http://TODO).

Below, you can find a selection of figures and graphs representing
different aspects of your Tinder usage. To produce an even more
comprehensive picture, you can provide the site with additional data! 
''')

            ]),

            html.Div([four_cards(data)], id="four_cards"),

            card_container("Sankey diagram", [sankey_graph(data)]),

            card_container("Development over time", [tabs(data)]),
            ], 
        className="container")
        ],
        id = "main-dash-app",
        className="bg-light-grey"
)
    return layout
