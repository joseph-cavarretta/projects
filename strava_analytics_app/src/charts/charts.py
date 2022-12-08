"""
Created on Dec 7, 2022 19:11:23
Created by Joe Cavarretta
"""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

DATA = pd.read_csv('data/processed_activities.csv')
NON_AEROBIC = ['AlpineSki', 'WeightTraining', 'Workout', 'RockClimbing']
STRENGTH = ['WeightTraining', 'RockClimbing']
MONTHS = {
        "month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    }


def max_elevation_scatter_plot(dataframe):
    plot_cols = ['month', 'day_of_month', 'year', 'name', 'type', 'hours', 'total_elevation_gain']
    sort_cols = ['day_of_month', 'month', 'total_elevation_gain']
    dups_cols = ['day_of_month', 'month']
    plot_data = dataframe.loc[~dataframe['type'].isin(NON_AEROBIC)]
    
    scatter = px.scatter(
        plot_data.sort_values(by=sort_cols, ascending=False).drop_duplicates(subset=dups_cols)[plot_cols], 
        x='month', 
        y='day_of_month', 
        color='total_elevation_gain', 
        size='hours',
        custom_data=['year', 'name', 'total_elevation_gain', 'type'],
        category_orders=MONTHS
    )
    scatter.update_traces(
        hovertemplate="<br>".join([
            "Name: %{customdata[1]}",
            "Type: %{customdata[3]}",
            "Date: %{x} %{y}, %{customdata[0]}",
            "Elevation: %{customdata[2]}",
        ])
    )
    return scatter.show()


def stacked_elevation_gain_by_month(dataframe):
    data_filtered = dataframe.loc[~dataframe['type'].isin(NON_AEROBIC)]
    data_grouped = data_filtered.groupby(['month', 'year']).agg({'total_elevation_gain': 'sum'}).reset_index()
    bar = px.bar(
        data_grouped, 
        x="month", 
        y="total_elevation_gain", 
        title='Total Elevation Gain by Month', 
        color='year',
        custom_data=['year'],
        category_orders=MONTHS
    )
    bar.update_traces(
        hovertemplate="<br>".join([
            "Month: %{x}",
            "Year: %{customdata[0]}",
            "Elevation: %{y:,}"
        ])
    )
    return bar.show()