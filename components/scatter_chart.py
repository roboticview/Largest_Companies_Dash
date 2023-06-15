import plotly.express as px
from dash import Dash, html, dcc

def render(app, data):
    data = data.iloc[1:]
    x = data['trillions']  
    y =  data['country']
    c = data['marketcap']
    s = data['marketcap']
    fig = px.scatter(
                    x=x, 
                    y=y, 
                    color=c,
                    size=s)
    return html.Div(dcc.Graph(figure=fig),id="scatter_chart")