import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np

def create_sankey(data):
    sankey_data = go.Sankey(
    node = dict(
      pad = 0,
      x = [0, 1/3, 1/3, 2/3, 2/3, 1, 1],
      y = [0.000001, 1., 0.3, 0.45, .8, .3, .6],

      thickness = 20, 
      line = dict(color = "black", width = 0.1, ),
      label = ["Total swipes", "Right swipes", "Left swipes", "Matches", "No Match", "No Messaging", "Messaging"],
      color = ["blue","blue", "red", "blue", "red", "blue", "red"],

      hovertemplate ="%{label}"#: %{value}"
    ),
    #arrangement= "snap",
    link = dict(
      source = [0, 0, 1, 1, 3, 3], # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = [1, 2, 3, 4, 5, 6],
      value = [data["swipes_likes_total"], data["swipes_passes_total"],
             data["matches_total"], data["no_match_total"], 
             data["no_messaging"], data["messaging"]],
      hoverinfo="skip",
      #color = ["black", "red", "red", "red", "red", "red", "red"]
    ),
    textfont=dict(size=20)
    )
    return sankey_data

def create_sankey_small(data):
    sankey_data = go.Sankey(
    node = dict(
      pad = 0,
      x = [0, 1/3, 1/3, 2/3, 2/3, 1, 1],
      y = [0.000001, 1., 0.3, 0.45, .8, .3, .6],

      thickness = 20, 
      line = dict(color = "black", width = 0.1, ),
      label = ["Total swipes", "Right swipes", "Left swipes", "Matches", "No Match", "No Messaging", "Messaging"],
      color = ["blue","blue", "red", "blue", "red", "blue", "red"],

      hovertemplate ="%{label}"#: %{value}"
    ),
    #arrangement= "snap",
    link = dict(
      source = [0, 0, 1, 1, 3, 3], # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = [1, 2, 3, 4, 5, 6],
      value = [data["swipes_likes_total"], data["swipes_passes_total"],
             data["matches_total"], data["no_match_total"], 
             data["no_messaging"], data["messaging"]],
      hoverinfo="skip",
      #color = ["black", "red", "red", "red", "red", "red", "red"]
    ),
    textfont=dict(size=20),       
    domain=dict(x=[0.6, 1], y =[0.6, 1])
    )

    return sankey_data

def sankey_graph(data):
    graph = dcc.Graph(
        id='sankey-graph',
        figure=go.Figure(data=[create_sankey(data)]),
        config={'displayModeBar': False}
    )
    return graph

def double_sankey(data):
    graph = dcc.Graph(
        id='sankey-graph',
        figure=double_plot(create_sankey(data), create_sankey_small(data)),
        config={'displayModeBar': False}
    )
    return graph


def double_plot(data1, data2):
    data = [data1, data2]
    layout = go.Layout(
    template="plotly_white",
    opacity=0.5
        )
    return go.Figure(data=data, layout=layout)
