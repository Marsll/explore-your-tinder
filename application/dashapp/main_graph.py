import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objects as go
from flask import current_app as app
import logging

def create_sankey(node_dict, link_dict):
    try:
        sankey_data = go.Sankey(
        node = node_dict,
        link = link_dict,
        textfont=dict(size=20)
        )
    except AttributeError:
        print("Something went wrong")
        sankey_data = go.Sankey(
        node = node_dict,
        link = link_dict,
        textfont=dict(size=20)
        )
    return sankey_data

def get_dicts(data):
    label = ["Total swipes", "Right swipes", "Left swipes", "Matches", "No Match", "Messaging", "No Messaging"]
    color = ["blue","blue", "red", "blue", "red", "blue", "red"]
    value = [data["swipes_likes_total"], data["swipes_passes_total"],
             data["matches_total"], data["no_match_total"], 
             data["messaging"], data["no_messaging"]]
    label, color, value, vertices = add_categories(data, label, color, value, vertices=4)
    x_vertices = np.tile(np.linspace(0, 1, vertices), 2)
    x_vertices.sort()
    y_pos = [0.000001, 1., 0.3, 0.45, .8, .3, .6, 0.1 , 0.5, 0.2]
    num_values = vertices * 2 - 1
    num_edges = vertices * 2
    source = [0, 0, 1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 9, 9]
    target = np.arange(vertices * 2) + 1
    node_dict = dict(
      pad = 0,
      x = x_vertices[1:],
      y = y_pos[:num_values],

      thickness = 20, 
      line = dict(color = "black", width = 0.1, ),
      label = label[:num_values],
      color = color[:num_values],

      hovertemplate ="%{label}"#: %{value}"
    )
    link_dict = dict(
      source = source[:num_edges], # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = value,
      hoverinfo="skip",
    )
    return node_dict, link_dict

def sankey_graph(data, id):
    node_dict, link_dict = get_dicts(data)

    graph = dcc.Graph(
        id=id,
        figure=go.Figure(data=[create_sankey(node_dict, link_dict)]),
        config={'displayModeBar': False, "staticPlot": True}
    )
    return graph




def add_categories(data, label, color, value, vertices=4):

    if data['numbers'] is not None and data['numbers'] != 0:
        vertices += 1
        label += ["Number", "No Number"]
        color += ["blue", "red"]
        numbers = data["numbers"]
        value += [numbers]
        value += [value[-3] - numbers]
    if data['dates'] is not None and data['dates'] != 0:
        vertices += 1
        label += ["Date", "No Date"]
        color += ["blue", "red"]
        dates = data["dates"]
        value += [dates]
        value += [value[-3] - dates]
    if data['outcomes'] is not None:
        vertices += 2
        label += ["Hookup", "F+", "Relationship", "Nothing"]
        color += 4 * ["green"]
    return label, color, value, vertices

















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



def double_sankey(data):
    graph = dcc.Graph(
        id='sankey-graph',
        figure=double_plot(create_sankey(data), create_sankey_small(data)),
        config={'displayModeBar': False, "staticPlot": True}
    )
    return graph


def double_plot(data1, data2):
    data = [data1, data2]
    layout = go.Layout(
    template="plotly_white",
    opacity=0.5
        )
    return go.Figure(data=data, layout=layout)
