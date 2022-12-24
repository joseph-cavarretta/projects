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
FONT = 'Open Sans,Light 300'
TITLE_FONT = 'Open Sans, Medium 500'
TABLE_HEADER_PROPS = {
    'fill_color': '#FF8303',
    'align': 'left',
    'line_color': 'white',
    'font': dict(color='white', size=13, family=TITLE_FONT)
}
TABLE_PROPS = {
    'fill_color': '#FEDEBE',
    'align': 'left',
    'line_color': 'white',
    'height': 28,
    'font': dict(color='black', size=11, family=FONT)
}
BAR_PROPS = {
    'bg_color': '#FEDEBE',
    'bar_color': '#FF8303',
    'font': FONT
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
    return scatter


def stacked_bar_by_month(dataframe, y=None, title=None, color=None):
    df = dataframe
    barchart = px.bar(
        df, 
        x="month", 
        y=y, 
        title=title, 
        color=color,
        custom_data=['year'],
        category_orders=MONTHS
    )
    barchart.update_traces(
        hovertemplate="<br>".join([
            "Month: %{x}",
            "Year: %{customdata[0]}",
            "Elevation: %{y:,}"
        ])
    )
    return barchart


def table(dataframe, cols=[], title=None):
    df = dataframe
    df = df.loc[:, cols]
    df.loc[df.name.str.len() > 38, 'name'] = df.loc[df.name.str.len() > 38, 'name'].str.slice(0,35) + '...'
    table = go.Figure(
        data=[
            go.Table(
                columnwidth = [45, 10, 15, 20],
                header=dict(
                    values=list(df.columns),
                    fill_color=TABLE_HEADER_PROPS['fill_color'],
                    align=TABLE_HEADER_PROPS['align'],
                    line_color=TABLE_HEADER_PROPS['line_color'],
                    font=TABLE_HEADER_PROPS['font']
                    
                ),
                cells=dict(
                    values=[df[col] for col in df.columns],
                    fill_color=TABLE_PROPS['fill_color'],
                    align=TABLE_PROPS['align'],
                    line_color=TABLE_PROPS['line_color'],
                    font=TABLE_PROPS['font'],
                    height=TABLE_PROPS['height']
                ))])
    table.update_layout(
        margin = dict(l=10, r=10, t=30, b=2),
        title = dict(text=title, y=0.99, x=0.025),
        title_font_family=TITLE_FONT
    )
    return table


def bar_chart_by_week(dataframe, x=None, y=None, title=None):
    df = dataframe
    barchart = px.bar(
        df, 
        x=x,
        y=y,
        title=title,
        color_discrete_sequence=[BAR_PROPS['bar_color']] * len(df)
    )
    barchart.update_layout(
        margin=dict(l=15, r=15, t=30, b=2),
        plot_bgcolor=BAR_PROPS['bg_color'],
        font_family=BAR_PROPS['font'],
        title_font_family=TITLE_FONT,
        xaxis_title=''
    )
    return barchart