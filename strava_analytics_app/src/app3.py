from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import charts as charts
import navigation

BACKGROUND_COLOR = '#282C34'
df = pd.read_csv('data/processed_activities.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.layout = html.Div(children=[
    navigation.navbar,
    html.Div(children=[
        dcc.Graph(
            id="table1", 
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%',
                'margin-top':'2%'
            },
            figure=charts.table(
                df.loc[~df.type.isin(charts.NON_AEROBIC)].sort_values(by='elevation', ascending=False).head(10),
                cols=['name', 'type', 'date', 'elevation'],
                title='Top 10 Activities by Elevation Gain'
            )
        ),
        dcc.Graph(
            id="table2",
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%',
                'margin-top':'2%'
            },
            figure=charts.table(
                df.loc[df.type=='Run'].sort_values(by='miles', ascending=False).head(10),
                cols=['name', 'type', 'date', 'miles'],
                title='Top 10 Runs by Distance'
            )
        ),
        dcc.Graph(
            id="table3", 
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%',
                'margin-top':'2%'
            },
            figure=charts.table(
                df.loc[df.type=='Ride'].sort_values(by='miles', ascending=False).head(10),
                cols=['name', 'type', 'date', 'miles'],
                title='Top 10 Rides by Distance'
            )
        )
    ], style={'margin-left':'1%'}) 
], 
    style={'background-color':BACKGROUND_COLOR}
)

if __name__ == '__main__':
    app.run_server(debug=True)