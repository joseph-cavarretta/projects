"""
Created on Mon Apr 5 23:19:28 2021
@author: joseph.cavarretta
"""
import pandas as pd
import requests
import json
import time
import configparser

def main():
    get_activities()


def get_activities():
    my_config_parser = configparser.ConfigParser()
    my_config_parser.read('secret/strava_API.config')
    client_id = my_config_parser.get('DEFAULT', 'client_id')
    client_secret = my_config_parser.get('DEFAULT', 'client_secret')

    with open('secret/strava_tokens.json') as json_file:
        strava_tokens = json.load(json_file)

    # if access_token has expired then use the refresh_token to get the new one
    if strava_tokens['expires_at'] < time.time():
        # make Strava auth API call with current refresh token
        response = requests.post(
                        url = 'https://www.strava.com/oauth/token',
                        data = {
                            'client_id': f'{client_id}',
                            'client_secret': f'{client_secret}',
                            'grant_type': 'refresh_token',
                            'refresh_token': strava_tokens['refresh_token']
                        }
        )
        new_strava_tokens = response.json()
        # save new tokens to file
        with open('secret/strava_tokens.json', 'w') as outfile:
            json.dump(new_strava_tokens, outfile)
        # use new Strava tokens from now
        strava_tokens = new_strava_tokens

    # loop through all activities
    page = 1
    url = "https://www.strava.com/api/v3/activities"
    access_token = strava_tokens['access_token']

    # create the dataframe ready for the API call to store your activity data
    activities = pd.DataFrame(
        columns = [
            "id",
            "name",
            "start_date_local",
            "type",
            "distance",
            "moving_time",
            "elapsed_time",
            "total_elevation_gain"
        ]
    )

    while True:
        # get page of activities from Strava
        r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
        r = r.json()

        # if no results then exit loop
        if (not r):
            break

        # add data to dataframe
        for x in range(len(r)):
            activities.loc[x + (page-1)*200,'id'] = r[x]['id']
            activities.loc[x + (page-1)*200,'name'] = r[x]['name']
            activities.loc[x + (page-1)*200,'start_date_local'] = r[x]['start_date_local']
            activities.loc[x + (page-1)*200,'type'] = r[x]['type']
            activities.loc[x + (page-1)*200,'distance'] = r[x]['distance']
            activities.loc[x + (page-1)*200,'moving_time'] = r[x]['moving_time']
            activities.loc[x + (page-1)*200,'elapsed_time'] = r[x]['elapsed_time']
            activities.loc[x + (page-1)*200,'total_elevation_gain'] = r[x]['total_elevation_gain']
        # increment page
        page += 1
        
    activities.to_csv('data/strava_activities_raw.csv', index=False)
    print ('Activity file updated!')


if __name__ == '__main__':
    main()