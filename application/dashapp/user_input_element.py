import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html


def generate_user_input_element():
    ele = html.Div([
        daq.ToggleSwitch(
            id='my-toggle-switch',
            value=False
        ),
        html.Div(id='toggle-switch-output')]
    )
    return ele
