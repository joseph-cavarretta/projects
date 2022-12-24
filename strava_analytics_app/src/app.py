# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import charts as charts


app = Dash(__name__)
df = pd.read_csv('data/processed_activities.csv')

app.layout = html.Div(children=[
    html.H1(children='Mountain Stats', style={'font': 'Open Sans'}),
    #dcc.Dropdown(),
    html.Div(children=[
        dcc.Graph(
            id="table1", 
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '33%'
            },
            figure=charts.table(
                df.loc[~df.type.isin(charts.NON_AEROBIC)].sort_values(by='elevation_gain', ascending=False).head(10),
                cols=['name', 'type', 'date', 'elevation_gain'],
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
                'width': '50%',
                'margin-top': '-5%'
            },
            figure=charts.bar_chart_by_week(
                df.loc[~df.type.isin(charts.NON_AEROBIC)].groupby(['year_week']).agg({'hours': 'sum'}).sort_values(by='year_week', ascending=False).reset_index().head(24).sort_values(by='year_week', ascending=True),
                x='year_week',
                y='hours',
                title='Aerobic Duration by Week'
            )
        ),
        dcc.Graph(
            id="bar2",
            style={
                'display': 'inline-block',
                'vertical-align': 'top',
                'width': '50%',
                'margin-top': '-5%'
            },
            figure=charts.bar_chart_by_week(
                df.loc[df.type=='WeightTraining'].groupby(['year_week']).agg({'hours': 'sum'}).sort_values(by='year_week', ascending=False).reset_index().head(24).sort_values(by='year_week', ascending=True),
                x='year_week',
                y='hours',
                title='Strength Duration by Week'
            )
        ),
    ]),
])


if __name__ == '__main__':
    app.run_server(debug=True)
