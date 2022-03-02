# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:19:28 2021

@author: joseph
"""

import pandas as pd
import numpy as np
import requests
import json
import time
from datetime import datetime
import calendar
from strava_API import strava_get_activities

#################### REQUEST STRAVA API TO GET ACTIVITES #######################

# this function pulls all strava activities and saves them to strava_activities_raw.csv
strava_get_activities()

#################### LOAD CSV WITH UPDATED DATA ################################

df = pd.read_csv('strava_activities_raw.csv')

#################### CONVERT & FORMAT DATA #####################################

#df['elapsed_time'] = pd.to_datetime(df['elapsed_time'], unit='s').dt.time
#df['moving_time'] = pd.to_datetime(df['moving_time'], unit='s').dt.time

#change start date local to datetime
df['start_date_local'] = pd.to_datetime(df['start_date_local'])

#create columns for year and month
df['day_of_month'] = df['start_date_local'].dt.day
df['day_of_year'] = df['start_date_local'].dt.dayofyear
df['week'] = df['start_date_local'].dt.isocalendar().week
df['month'] = df['start_date_local'].dt.month_name()
df['year'] = df['start_date_local'].dt.year

#change start date to only show date
df['start_date_local'] = pd.to_datetime(df['start_date_local']).dt.date

#convert distance to miles
meters_to_miles_convert = 0.000621371
df['distance'] = (df['distance'] * meters_to_miles_convert).astype(float).round(2)
df.rename(columns={'distance': 'miles'}, inplace=True)

#convert elevation gain to feet
meters_to_feet_convert = 3.28084
df['total_elevation_gain'] = (df['total_elevation_gain'] * meters_to_feet_convert).astype(float).round(2)

#################### BEAR PEAK COUNT ###########################################

# Create column in original dataframe that detects and labels it as a bear peak 1 if True 0 if False
df['bear_peak_count'] = np.where((df['name'].str.contains('Bear Peak', case = False, na = False) &
                                   ~df['name'].str.contains('Bear Peak x', case = False, na = False)) |
                                   df['name'].str.contains('Skyline', case = False, na = False), 1, 0)

# Create helper column since I can't figure out how to iterate through columns of series for a substring
df['is_a_bear']= np.where(df['name'].str.contains('Bear Peak', case = False, na = False) &
                                  ~df['name'].str.contains('Summit Repeat', case = False, na = False),
                                  df['name'], np.nan)

# Use helper column to add bear peak multiples to bear_peak count column. I need to subtract 1 from these somehow
df['bear_peak_count']=df['bear_peak_count']+pd.to_numeric(df['is_a_bear'].str[-1],errors='coerce').fillna(0).astype(int)

# Create helper column for summit repeats
df['summit_repeats'] = np.where(df['name'].str.contains('summit repeats', case = False, na = False),
                                        df['name'].str[-1:], '')

# Use summit repeats helper column to add to bear peak counts
df['bear_peak_count']=df['bear_peak_count']+pd.to_numeric(df['summit_repeats'].str[-1],errors='coerce').fillna(0).astype(int)

# don't need this groupby right now, can delete later
bear_peak_count = df.groupby(['year'])['bear_peak_count'].sum().reset_index().set_index('year')

bear_peak_count_all_time = df['bear_peak_count'].sum()
bear_peak_count_2016 = df['bear_peak_count'][df['year'] == 2016].sum()
bear_peak_count_2017 = df['bear_peak_count'][df['year'] == 2017].sum()
bear_peak_count_2018 = df['bear_peak_count'][df['year'] == 2018].sum()
bear_peak_count_2019 = df['bear_peak_count'][df['year'] == 2019].sum()
bear_peak_count_2020 = df['bear_peak_count'][df['year'] == 2020].sum()
bear_peak_count_2021 = df['bear_peak_count'][df['year'] == 2021].sum()

# Drop unneeded columns
df = df.drop(labels=['is_a_bear', 'summit_repeats'], axis=1)

# add trend against best year?
# further analysis on avg rate of ascent, avg ascent time, best time, etc..

#################### SANITAS COUNT #############################################

df['sanitas'] = np.where((df['name'].str.contains('Sanitas', case = False, na = False)
                                  & ~df['name'].str.contains('Sanitas x', case = False, na = False))
                                  | df['name'].str.contains('Skyline', case = False, na = False), 1,
                                       np.where(df['name'].str.contains('Sanitas x', case = False, na = False),
                                                 df['name'].str[-1], 0))

df['sanitas'] = df['sanitas'].astype(int)

sanitas_count_all_time = df['sanitas'].sum()
sanitas_count_2016 = df['sanitas'][df['year'] == 2016].sum()
sanitas_count_2017 = df['sanitas'][df['year'] == 2017].sum()
sanitas_count_2018 = df['sanitas'][df['year'] == 2018].sum()
sanitas_count_2019 = df['sanitas'][df['year'] == 2019].sum()
sanitas_count_2020 = df['sanitas'][df['year'] == 2020].sum()
sanitas_count_2021 = df['sanitas'][df['year'] == 2021].sum()

#################### 2ND FLATIRON COUNT ########################################

df['2nd_flatiron'] = np.where(df['name'].str.contains('2nd Flatiron', case = False, na = False)
                                      & ~df['name'].str.contains('2nd Flatiron x', case = False, na = False), 1,
                                          np.where(df['name'].str.contains('2nd Flatiron x', case = False, na = False),
                                               (df['name'].str[-1]), 0))

df['2nd_flatiron'] = df['2nd_flatiron'].astype(int)

freeway_count_all_time = df['2nd_flatiron'].sum()
freeway_count_2016 = df['2nd_flatiron'][df['year'] == 2016].sum()
freeway_count_2017 = df['2nd_flatiron'][df['year'] == 2017].sum()
freeway_count_2018 = df['2nd_flatiron'][df['year'] == 2018].sum()
freeway_count_2019 = df['2nd_flatiron'][df['year'] == 2019].sum()
freeway_count_2020 = df['2nd_flatiron'][df['year'] == 2020].sum()
freeway_count_2021 = df['2nd_flatiron'][df['year'] == 2021].sum()

# add in total scrambles

#################### COUNT OF STRENGTH #########################################

df['climb'] = np.where(df['name'].str.contains('Climb', case = False, na = False), 1, 0)
df['bouldering'] = np.where(df['name'].str.contains('Bouldering', case = False, na = False), 1, 0)
df['plyo'] = np.where(df['name'].str.contains('Plyo', case = False, na = False), 1, 0)
df['strength'] = np.where(df['name'].str.contains('Strength', case = False, na = False), 1, 0)

climb_count_all_time = df['climb'].sum()
climb_count_2020 = df['climb'][df['year'] == 2020].sum()
climb_count_2021 = df['climb'][df['year'] == 2021].sum()

boulder_count_all_time = df['bouldering'].sum()
boulder_count_2020 = df['bouldering'][df['year'] == 2020].sum()
boulder_count_2021 = df['bouldering'][df['year'] == 2021].sum()

plyo_count_all_time = 0
plyo_count_2020 = df['plyo'][df['year'] == 2020].sum()
plyo_count_2021 = df['plyo'][df['year'] == 2021].sum()

strength_count_all_time = 0
strength_count_2020 = df['strength'][df['year'] == 2020].sum()
strength_count_2021 = df['strength'][df['year'] == 2021].sum()

# number of pitches climbs
# number of boulder routes
# breakdown by grade for each
### add in list / count of 14ers
## have a running list of 14ers and their counts of ascents with note tag 14er


#################### ANALYZE DATA ##############################################

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

df.to_csv('strava_activities_final.csv', index = False)
