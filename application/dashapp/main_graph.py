from contextlib import suppress

import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objects as go
from flask import current_app as app
import logging

def create_sankey(node_dict, link_dict):
    sankey_data = go.Sankey(
            node = node_dict,
            link = link_dict,
            textfont=dict(size=20)
    )
    return sankey_data


def sankey_graph(data, id):
    node_dict, link_dict = get_dicts(data)

    graph = dcc.Graph(
        id=id,
        figure=go.Figure(data=[create_sankey(node_dict, link_dict)]),
        config={'displayModeBar': False, "staticPlot": True}
    )
    return graph

def get_dicts(data):
    label = ["Total swipes", "Right swipes", "Left swipes", "Matches", "No Match", "Messaging", "No Messaging"]
    color = ["blue","blue", "red", "blue", "red", "blue", "red"]
    value = [data["swipes_likes_total"], data["swipes_passes_total"],
             data["matches_total"], data["no_match_total"], 
             data["messaging"], data["no_messaging"]]
    label, color, value, vertices, other = add_categories(data, label, color, value, vertices=4)
    if other != 0:
        x_vertices = np.tile(np.linspace(0, 1, vertices + 1), 2)
    else:
        x_vertices = np.tile(np.linspace(0, 1, vertices), 2)
    x_vertices.sort()
    num_values = vertices * 2 - 1
    num_edges = (vertices - 1) * 2
    y_pos = [0.000001, 1., 0.3, 0.45, .8, .3, .6, 0.5, 0.1, 0.3, 0.7][:num_values]
    # ensure that the graph looks nice for a right/total ratio > 50%
    if value[0] > value[1]:
        y_pos = [0.000001, 0.7, 0.1, 0.2, .8, .3, .6, 0.5, 0.1, 0.2, 0.7][:num_values]
        if value[2] > value[3]: 
            y_pos = [0.000001, 0.7, 0.1, 0.2, .8, .3, .8, 0.5, 0.1, 0.2, 0.7][:num_values]

    source = [0, 0, 1, 1, 3, 3, 5, 5, 7, 7, 9, 9][:num_edges]
    target = np.arange(vertices * 2 + other) + 1
    if other !=0:
        if value[0] > value[1]:
            y_pos += [0.01, 0.55, 0.35, .85][:other]
        else:
            y_pos += [0.01, 0.55, 0.15, .85][:other]
        x_vertices = np.concatenate([x_vertices, np.array([x_vertices[-1]] * (other - 2))])
        source += [source[-1] + 2] * other
        app.logger.info('value', x_vertices, source, target)

    node_dict = dict(
      pad = 0,
      x = x_vertices[1:],
      y = y_pos,

      thickness = 20, 
      line = dict(color = "black", width = 0.1, ),
      label = label,
      color = color ,

      hovertemplate ="%{label}"#: %{value}"
    )
    link_dict = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = value,
      hoverinfo="skip",
    )
    return node_dict, link_dict


def get_dicts_zoom(data):
    label = ["Matches", "Messaging", "No Messaging"]
    color = ["blue", "blue", "red"]
    value = [data["messaging"], data["no_messaging"]]
    label, color, value, vertices, other = add_categories(data, label, color, value, vertices=2)
    if other != 0:
        x_vertices = np.tile(np.linspace(0, 1, vertices + 1), 2)
    else:
        x_vertices = np.tile(np.linspace(0, 1, vertices), 2)
    x_vertices.sort()
    num_values = vertices * 2 - 1
    num_edges = (vertices - 1) * 2
    y_pos = [0.000001, 1., 0.3, 0.45, .8, .3, .6][:num_values]
    if value[0] > value[1]:
        y_pos = [0.000001, .8, 0.1, 0.2, .8, .3, .8][:num_values]

    source = [0, 0, 1, 1, 3, 3, 5, 5][:num_edges]
    target = np.arange(vertices * 2 + other) + 1
    if other !=0:
        if value[0] > value[1]:
            y_pos += [0.01, 0.55, 0.35, .85][:other]
        else:
            y_pos += [0.01, 0.55, 0.15, .85][:other]
        x_vertices = np.concatenate([x_vertices, np.array([x_vertices[-1]] * (other - 2))])
        if source[-1] == 0:
            source += [1] * other
        else:
            source += [source[-1] + 2] * other
        app.logger.info('value', x_vertices, source, target)

    # x_vertices = np.tile(np.linspace(0, 1, vertices), 2)
    # x_vertices.sort()
    # y_pos = [0.000001, 1., 0.3, 0.45, .8, .3, .6, 0.1 , 0.5, 0.2]
    # num_values = vertices * 2 - 1
    # num_edges = vertices * 2
    # source = [0, 0, 1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 9, 9]
    # target = np.arange(vertices * 2) + 1
    #app.logger.info('value', value, target)
    node_dict = dict(
      pad = 0,
      x = x_vertices[1:],
      y = y_pos,

      thickness = 20, 
      line = dict(color = "black", width = 0.1, ),
      label = label,
      color = color,

      hovertemplate ="%{label}"#: %{value}"
    )
    link_dict = dict(
      source = source, # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = target,
      value = value,
      hoverinfo="skip",
    )
    return node_dict, link_dict


def add_categories(data, label, color, value, vertices):
    other = 0
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
    hookups = data['hookups']
    fplus = data['f+s']
    relationship = data['relationships']
    nothing = data['nothing']
    difference = value[-2]
    if hookups:
        label += ["Hookups"]
        color += ['green']
        value += [hookups]
        difference -= hookups
        other += 1
    if fplus:
        label += ["F+s"]
        color += ['green']
        value += [fplus]
        difference -= fplus
        other += 1
    if relationship:
        label += ["Relationships"]
        color += ['green']
        value += [relationship]
        difference -= relationship
        other += 1
    if hookups or fplus or relationship or nothing:
        if nothing is None:
            value +=[difference]
        else:
            value += [nothing]
        label += ["Nothing"]
        color += ['green']
        other += 1
    return label, color, value, vertices, other












####### old functions unused #############




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
