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

  # Plot the figure
def cumulative_graph(data):
    graph = dcc.Graph(
        id='sankey-graph',
        figure=create_cumulative(data),
        config={'displayModeBar': False, "staticPlot": True}
    )
    return graph
 