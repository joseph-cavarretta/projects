"""
Created on Fri Sept 2 18:02:33 2022
@author: joseph.cavarretta
"""
import pandas as pd


def main():
    df = load_data()
    years = get_years()
    
    metrics = [
        'bear_peak_count',
        'sanitas_count',
        '2nd_flatiron_count',
        'strength_count',

    ]
    for metric in metrics:
        generate_yearly_activity_counts(metric=metric)
        generate_yearly_activity_durations(metric=metric)




# don't need this groupby right now, can delete later
bear_peak_count = df.groupby(['year'])['bear_peak_count'].sum().reset_index().set_index('year')

bear_peak_count_all_time = df['bear_peak_count'].sum()
bear_peak_count_2016 = df['bear_peak_count'][df['year'] == 2016].sum()
bear_peak_count_2017 = df['bear_peak_count'][df['year'] == 2017].sum()
bear_peak_count_2018 = df['bear_peak_count'][df['year'] == 2018].sum()
bear_peak_count_2019 = df['bear_peak_count'][df['year'] == 2019].sum()
bear_peak_count_2020 = df['bear_peak_count'][df['year'] == 2020].sum()
bear_peak_count_2021 = df['bear_peak_count'][df['year'] == 2021].sum()

# add trend against best year?
# further analysis on avg rate of ascent, avg ascent time, best time, etc..

sanitas_count_all_time = df['sanitas'].sum()
sanitas_count_2016 = df['sanitas'][df['year'] == 2016].sum()
sanitas_count_2017 = df['sanitas'][df['year'] == 2017].sum()
sanitas_count_2018 = df['sanitas'][df['year'] == 2018].sum()
sanitas_count_2019 = df['sanitas'][df['year'] == 2019].sum()
sanitas_count_2020 = df['sanitas'][df['year'] == 2020].sum()
sanitas_count_2021 = df['sanitas'][df['year'] == 2021].sum()

##### ELEVATION x YEAR #####
elev_totals = df.groupby(['year'])['total_elevation_gain'].sum().reset_index()

elev_total_2016 = elev_totals['total_elevation_gain'][elev_totals['year'] == 2016].values[0]
elev_total_2017 = elev_totals['total_elevation_gain'][elev_totals['year'] == 2017].values[0]
elev_total_2018 = elev_totals['total_elevation_gain'][elev_totals['year'] == 2018].values[0]
elev_total_2019 = elev_totals['total_elevation_gain'][elev_totals['year'] == 2019].values[0]
elev_total_2020 = elev_totals['total_elevation_gain'][elev_totals['year'] == 2020].values[0]
elev_total_2021 = elev_totals['total_elevation_gain'][elev_totals['year'] == 2021].values[0] # this will just be an ongoing updated current value

# how to compare progress for previous years at same date?

#####  COUNT OF ACTIVITES x YEAR #####
group_keys = ['name', 'moving_time', 'elapsed_time']
activity_stats = df.groupby(['year', 'type'])[group_keys].agg({'name': 'count',
                                                                           'moving_time': 'sum',
                                                                           'elapsed_time': 'sum'}).reset_index()

total_activities_count_2021 = activity_stats.loc[(activity_stats['year'] == 2021), 'name'].sum()

run_activities_count_2021 = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='Run')]['name'].squeeze()

bike_activities_count_2021 = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='Bike')]['name'].squeeze()

strength_activities_count_2021 = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='WeightTraining')]['name'].squeeze()

climb_activities_count_2021 = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='RockClimbing')]['name'].squeeze()

skimo_activities_count_2021 = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='BackcountrySki')]['name'].squeeze()

##### ACTIVITY DURATION THIS YEAR #####
# Sum of duration is included in df = activity_stats
activity_duration_moving_2021 = activity_stats.loc[(activity_stats['year'] == 2021), 'moving_time'].sum()
activity_duration_total_2021 = activity_stats.loc[(activity_stats['year'] == 2021), 'elapsed_time'].sum()

run_duration = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='Run')]['elapsed_time'].squeeze()

bike_duration_2021 = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='Bike')]['elapsed_time'].squeeze()

strength_duration_2021 = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='WeightTraining')]['elapsed_time'].squeeze()

climb_activities_duration_2021 = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='RockClimbing')]['elapsed_time'].squeeze()

skimo_activities_duration_2021 = activity_stats.loc[(activity_stats['year']==2021) &
                                                        (activity_stats['type']=='BackcountrySki')]['elapsed_time'].squeeze()
# number of pitches climbs
# number of boulder routes
# breakdown by grade for each