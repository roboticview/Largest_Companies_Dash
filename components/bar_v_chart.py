import plotly.express as px
from dash import Dash, html, dcc

def render(app,data):
    
    fig = px.bar(data, x='country', y='trillions')
    return html.Div(dcc.Graph(figure=fig), id="barv_chart")