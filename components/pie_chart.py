from dash import Dash, html, dcc
import plotly.express as px


def render(app,data):
    fig = px.pie(data, values='trillions', names='country', title='Market cap by country')
    return html.Div(dcc.Graph(figure=fig), id="pie_chart")
