import plotly.express as px
from dash import Dash, html, dcc


def render(app,data):
    fig = px.bar(data, x='trillions', y='country', orientation='h')
    return html.Div(dcc.Graph(figure=fig),id="Bar_Chart")