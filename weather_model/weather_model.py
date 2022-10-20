# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:31:22 2022
@author: joseph
"""
#from weather_model import isolation_model
from datetime import datetime, timedelta
from meteostat import Stations, Daily
import pandas as pd
import numpy as np
import joblib

df = pd.read_csv('data/labelled_weather_data.csv')

# if first time adding data:
if len(df) == 0:
    now = datetime.now()
    # start with yesterday's data
    end = datetime(now.year,now.month,now.day) - timedelta(days=1)
    start = end

else:
    now = datetime.now()
    start = df['date'].iloc[-1] + timedelta(days=1)
    # capture all data up until yesterday
    end = datetime(now.year,now.month,now.day) + timedelta(days=1)

# create Point for Boulder, CO
#boulder = Point(40.014986,-105.270546, 1620)

# pull nearest weather station to coordinates from weather model training data
stations = Stations()
stations = stations.nearby(40.014986,-105.270546)
station = stations.fetch(1).reset_index()
station_id = station['id'][0]

# get daily data
data = Daily(
    #boulder,
    station_id,
    start,
    end
    )
data = data.fetch()
#data.index = data.index.strftime('%Y/%m/%d')

data = data[['tavg']]
data.index.name = 'date'
data.reset_index(inplace=True)
data['date'] = data['date'].dt.strftime('%Y-%m-%d')

# the data above does not reflect the same values I see in manually checking weather.
# there is variation in how the weather data is reported
# however to demonstrate the process, I will use it for now.

isolation_forest = joblib.load("isolation_forest.pkl")

test_data = np.array(data['tavg']).reshape(-1,1)
labels = isolation_forest.predict(test_data)

data['anomaly_score'] = labels
data['anomaly'] = np.where(data['anomaly_score'] == -1, True, False)

# not appending new data to original training data until new data is more reliable
df = df.append(data)
df.to_csv('labelled_weather_data.csv', index=False)
