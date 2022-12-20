# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/processed_activities.csv')
# types to not want to include in rankings for distance and elevation
omit_types = ['AlpineSki', 'WeightTraining', 'Swim', 'Workout', 'RockClimbing', 'Elliptical']

# Bar chart of aerobic time for last 12 weeks
df['year_week'] = df['year'].astype(str) + '-' + df['week'].astype(str).str.zfill(2)
grouped_yr_wk = df.loc[~df.type.isin(omit_types)].groupby(['year_week']).agg({'hours': 'sum'}).sort_values(by='year_week', ascending=False).reset_index().head(20).sort_values(by='year_week', ascending=True)
time_x_week_bar = px.bar(grouped_yr_wk,
                          x="year_week",
                          y="hours",
                          title='Aerobic Training Time Last 20 Weeks'
                         )

from functools import reduce
dfs = [
    df.groupby('year').agg({'bear_peak_count':'sum'}).reset_index(),
    df.groupby('year').agg({'sanitas_count':'sum'}).reset_index(),
    df.groupby('year').agg({'second_flatiron_count':'sum'}).reset_index()
]

df_merged = reduce(lambda  left,right: pd.merge(left,right, on=['year'],
                                            how='left'), dfs)
# Count of bear peaks, sanitas, 2nd_flatiron by year
local_peaks = px.bar(
    data_frame=df_merged.loc[df_merged.year != 2015],
    x = 'year',
    y = ['bear_peak_count','sanitas_count','second_flatiron_count'],
    opacity = 0.9,
    orientation = "v",
    barmode = 'group',
    title='Most Common Routes Count by Year',
)

# Most active days of the year (based on max activity elevtion and time)
scatter = px.scatter(df.groupby(['day_of_month', 'month']).agg({'total_elevation_gain':'max',
                                                  'hours': 'max'}).reset_index(), 
                 x='month', 
                 y='day_of_month', 
                 color='total_elevation_gain', 
                 size='hours',
                 category_orders={"month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]})


app.layout = html.Div(children=[
    html.H1(children='Mountain Stats'),
    html.Div(children=''),
    dcc.Graph(
        id='example-graph',
        figure=time_x_week_bar
    ),
    dcc.Graph(
        id='example-graph2',
        figure=local_peaks
    ),
    dcc.Graph(
        id='example-graph3',
        figure=scatter
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
