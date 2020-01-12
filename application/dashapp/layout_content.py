import dash_core_components as dcc
import dash_daq as daq
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

            card_container("Sankey diagram", 
                [sankey_graph(data, id='sankey-graph'),
                dcc.Input(id='numbers', type='number', value=None, min=0, placeholder="Numbers"),
                dcc.Input(id='dates', type='number', value=None, min=0, placeholder="Dates"),
                dcc.Input(id='hookups', type='number', value=None, min=0, placeholder="Hookups"),
                dcc.Input(id='f+s', type='number', value=None, min=0, placeholder="F+"),
                dcc.Input(id='relationships', type='number', value=None, min=0, placeholder="Relationships"),
                dcc.Input(id='nothing', type='number', value=None, min=0, placeholder="Nothing"),
                html.Button('Submit', id='button'), 
                daq.ToggleSwitch(id='toggle-zoom', value=False)
                ]),

            card_container("Development over time", [tabs(data)]),
            ], 
        className="container")
        ],
        className="bg-light-grey"
)
    return layout
