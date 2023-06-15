from dash import Dash, html
import dash_bootstrap_components as dbc
from components import (
               pie_chart, 
               bar_chart,
               scatter_chart, 
               bar_v_chart
          )

def create_layout(app, data):
     heading = html.H1("Largest Companies by Country", className="bg-primary text-white p-2 mb-3")
     return dbc.Container(children=[
          heading,
          dbc.Row([
               dbc.Col(pie_chart.render(app, data),lg=6),
               dbc.Col(bar_chart.render(app, data),lg=6),
          ],className="mt-4"),
          dbc.Row([
               dbc.Col(scatter_chart.render(app, data),lg=6),
               dbc.Col(bar_v_chart.render(app, data),lg=6),
         ], className="mt-4"),
    ])