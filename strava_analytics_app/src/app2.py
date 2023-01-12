# visit http://127.0.0.1:8050/ in your web browser.

"""
SUMMARY PAGE
"""
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import charts as charts
import navigation

BACKGROUND_COLOR = '#282C34'

app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

df = pd.read_csv('data/processed_activities.csv')

app.layout = html.Div(children=[
    html.H1('Mountain Stats', id='header', style={'font-family': 'Arial', 'line-height': '50%', 'background-color': BACKGROUND_COLOR}),
    navigation.navbar,
    #html.H3('Overall Activity Summary', id='header3', style={'font-family': 'Arial', 'line-height': '50%', 'margin-bottom': '3%'}),
    html.Div(children=[
        dcc.Graph(
            id="table1", 
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%'
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
                'width': '33%'
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
                'width': '33%'
            },
            figure=charts.table(
                df.loc[df.type=='Ride'].sort_values(by='miles', ascending=False).head(10),
                cols=['name', 'type', 'date', 'miles'],
                title='Top 10 Rides by Distance'
            )
        )
    ]),
    html.Div(children=[
        dcc.Graph(
            id="bar1", 
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%',
                'margin-top': '-4%'
            },
            figure=charts.bar_chart_by_week(
                df.loc[~df.type.isin(charts.NON_AEROBIC)].groupby(['year_week']).agg({'hours': 'sum'}).sort_values(by='year_week', ascending=False).reset_index().head(20).sort_values(by='year_week', ascending=True),
                x='year_week',
                y='hours',
                title='Aerobic Duration (hrs) by Week'
            )
        ),
        dcc.Graph(
            id="bar2",
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%',
                'margin-top': '-4%'
            },
            figure=charts.bar_chart_by_week(
                df.loc[df.type=='WeightTraining'].groupby(['year_week']).agg({'hours': 'sum'}).sort_values(by='year_week', ascending=False).reset_index().head(20).sort_values(by='year_week', ascending=True),
                x='year_week',
                y='hours',
                title='Strength Duration (hrs) by Week'
            )
        ),
        dcc.Graph(
            id="bar3", 
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%',
                'margin-top': '-4%'
            },
            figure=charts.bar_chart_by_week(
                df.loc[~df.type.isin(charts.NON_AEROBIC)].groupby(['year_week']).agg({'elevation': 'sum'}).sort_values(by='year_week', ascending=False).reset_index().head(20).sort_values(by='year_week', ascending=True),
                x='year_week',
                y='elevation',
                title='Elevation Gain (ft) by Week'
            )
        )
    ]),
    html.Div(children=[
        dcc.Graph(
            id="bar4", 
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '50%',
                'margin-top': '1%'
            },
            figure=charts.local_peaks_bar(df)
        ),
        dcc.Graph(
            id="bar5",
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '50%',
                'margin-top': '1%'
            },
            figure=charts.scatter_max(df)
        )
    ]),
])

"""
To add:
- page
    - recent activity and fitness / fatigue
        - last 30 days of activity? Duration and type?
- page
    - summary overall stats and records
    - trending graph against other years (elevation line chart)
- page
    - run / ride / strength specific breakdowns
"""

if __name__ == '__main__':
    app.run_server(debug=True)
