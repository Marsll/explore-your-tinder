import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output, State
from .cumulative_swipes import cumulative_graph, cumulative_matches, cumulative_matchrate


def tabs(data):
    tabs = dcc.Tabs(id="tabs", children=[
    dcc.Tab(label='Swipes', children=[
        html.Div([cumulative_graph(data)]),
    ]),
    dcc.Tab(label='Matches', children=[
          html.Div([cumulative_matches(data)]),
    ]),
    dcc.Tab(label='Matchrate', children=[
        html.Div([cumulative_matchrate(data)])
        ]),
    ])
    return tabs
