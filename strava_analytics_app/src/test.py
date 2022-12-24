# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import charts as charts


app = Dash(__name__)
df = pd.read_csv('data/processed_activities.csv')

app.layout = html.Div(children=[
    html.H1(children='Mountain Stats'),
    #dcc.Dropdown(),
    html.Div(children=[
        dcc.Graph(
            id="graph1", 
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%'
            },
            figure=charts.table(
                df.loc[~df.type.isin(charts.NON_AEROBIC)].sort_values(by='elevation_gain', ascending=False).head(10),
                cols=['name', 'type', 'date', 'elevation_gain'],
                title='Top Activities by Elevation Gain'
            )
        ),
        dcc.Graph(
            id="graph2",
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%'
            },
            figure=charts.table(
                df.loc[df.type=='Run'].sort_values(by='miles', ascending=False).head(10),
                cols=['name', 'type', 'date', 'miles'],
                title='Top Runs by Distance'
            )
        ),
        dcc.Graph(
            id="graph3", 
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%'
            },
            figure=charts.table(
                df.loc[df.type=='Ride'].sort_values(by='miles', ascending=False).head(10),
                cols=['name', 'type', 'date', 'miles'],
                title='Top Rides by Distance'
            )
        )
    ]),
])


if __name__ == '__main__':
    app.run_server(debug=True)
