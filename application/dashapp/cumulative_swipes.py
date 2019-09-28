import plotly.graph_objs as go
import dash_core_components as dcc
import datetime


def create_cumulative(data):
    x = data["swipes_cum"]["dates"]
    y_total = data["swipes_cum"]["swipes_count"]
    y = data["swipes_likes_cum"]["swipes_count"]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_total, fill='tonexty',
                        mode= 'none', name="Total swipes"))
    fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy',
                        mode='none', # override default markers+lines,
                        name="Right swipes", 
                        ))

    fig.update_xaxes(showgrid=True, gridwidth=1., gridcolor='LightGrey')
    fig.update_yaxes(showgrid=True, gridwidth=1., gridcolor='LightGrey',)
    fig.update_layout(
    plot_bgcolor="White", 
    legend=go.layout.Legend(
        x=0.1,
        y=0.95 ,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=20,
            color="black"
        ),
        bgcolor="White",
        )
    )
    return fig

def create_cumulative_matches(data):
    x = data["matches_cum"]["dates"]
    y = data["matches_cum"]["swipes_count"]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, fill='tozeroy',
                        mode='none', 
                        name="Matches", 
                        ))

    fig.update_xaxes(showgrid=True, gridwidth=1., gridcolor='LightGrey')
    fig.update_yaxes(showgrid=True, gridwidth=1., gridcolor='LightGrey',)
    fig.update_layout(
    plot_bgcolor="White", 
    legend=go.layout.Legend(
        x=0.1,
        y=0.95 ,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=20,
            color="black"
        ),
        bgcolor="White",
        )
    )
    #fig.update_layout(showlegend=True)
    return fig

def create_matchrate(data):
    x = data["matches_cum"]["dates"]
    y = data["matchrate_cum"] 

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, 
                        name="Matchrate in %", 
                        ))

    fig.update_xaxes(showgrid=True, gridwidth=1., gridcolor='LightGrey')
    fig.update_yaxes(showgrid=True, gridwidth=1., gridcolor='LightGrey', 
                     tickformat= ',.0%')
    fig.update_layout(
    plot_bgcolor="White", 
    legend=go.layout.Legend(
        x=.9,
        y=1. ,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=20,
            color="black"
        ),
        bgcolor="White",
        )
    )
    #fig.update_layout(showlegend=True)
    return fig


  # Plot the figure
def cumulative_graph(data):
    graph = dcc.Graph(
        id='swipes_cum',
        figure=create_cumulative(data),
        config={'displayModeBar': False, "staticPlot": True}
    )
    return graph

def cumulative_matches(data):
    graph = dcc.Graph(
        id='matches_cum',
        figure=create_cumulative_matches(data),
        config={'displayModeBar': False, "staticPlot": True}
    )
    return graph

def cumulative_matchrate(data):
    graph = dcc.Graph(
        id='matchrate',
        figure=create_matchrate(data),
        config={'displayModeBar': False, "staticPlot": True}
    )
    return graph
 