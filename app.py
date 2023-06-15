from dash import Dash, html
import dash_bootstrap_components as dbc
from layout import create_layout
from util import get_contries_marketcap
import os

PATH = os.path.join(os.getcwd(),"LargestCompanies.csv")

def main():
    data = get_contries_marketcap(PATH)   
    app = Dash(external_stylesheets=[dbc.themes.COSMO])
    app.title = "Largest Companies"
    app.layout = create_layout(app, data)
    app.run()

if __name__=="__main__":
    main()