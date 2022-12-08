"""
Created on Nov 13, 2022 14:11:23
Created by Joe Cavarretta
"""
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from functools import reduce

app = dash.Dash()
df = pd.read_csv('data/processed_activities.csv')


app.layout = html.Div([
    html.H4('Restaurant tips by day of week'),
    dcc.Dropdown(
        id="dropdown",
        options=["Fri", "Sat", "Sun"],
        value="Fri",
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("dropdown", "value"))
def update_bar_chart(day):
    df = px.data.tips() # replace with your own data source
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", 
                 color="smoker", barmode="group")
    return fig


if __name__ == '__main__': 
    app.run_server()