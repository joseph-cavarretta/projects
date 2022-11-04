"""
Created on Mon Mar 14 21:31:22 2022
@author: joseph
"""
from datetime import datetime, timedelta
from meteostat import Stations, Daily
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

FILE_PATH = Path('src/data/labelled_weather_data.csv')
MODEL_PATH = Path('src/isolation_forest.pkl')


def main():
    df = read_data()
    start, end = get_data_start_end(df)
    new_data = get_new_data(start, end)
    labelled_data = label_new_data(new_data)
    write_file(df, labelled_data)


def read_data():
    df = pd.read_csv(FILE_PATH)
    return df


def get_data_start_end(dataframe):
    df = dataframe    
    # if first time adding data:
    if len(df) == 0:
        now = datetime.now()
        # start with yesterday's data
        end = datetime(now.year,now.month,now.day) - timedelta(days=1)
        start = end
    else:
        now = datetime.now()
        start = pd.to_datetime(df['date'].iloc[-1]) + timedelta(days=1)
        # capture all data up until yesterday
        end = datetime(now.year,now.month,now.day) + timedelta(days=1)
    return start, end


def get_new_data(start, end):
    stations = Stations()
    # pull nearest weather station to coordinates from weather model training data
    stations = stations.nearby(40.014986,-105.270546)
    station = stations.fetch(1).reset_index()
    station_id = station['id'][0]
    # get daily data
    data = Daily(
        station_id,
        start,
        end
        )
    data = data.fetch()
    data = data[['tavg']]
    data.index.name = 'date'
    data.reset_index(inplace=True)
    data['date'] = data['date'].dt.strftime('%Y-%m-%d')
    return data


def label_new_data(dataframe):
    data = dataframe.copy()
    isolation_forest = joblib.load(MODEL_PATH)

    test_data = np.array(data['tavg']).reshape(-1,1)
    labels = isolation_forest.predict(test_data)

    data['anomaly_score'] = labels
    data['anomaly'] = np.where(data['anomaly_score'] == -1, True, False)
    return data
    

def write_file(dataframe, labelled_data):
    df = dataframe
    df = pd.concat([df, labelled_data], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
    total_anomalies = len(df.loc[df['anomaly'] == True])
    print("Weather file updated.")
    print(f"Open {FILE_PATH} to check anomalies")
    print(f'There are {total_anomalies} days with anomalous weather logged')


if __name__ == '__main__':
    main()