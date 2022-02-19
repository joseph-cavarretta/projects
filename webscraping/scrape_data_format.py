# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 09:36:09 2021

@author: joe.cavarretta
"""

############### IMPORT LIBRARIES & SET FORMATS ###############
import pandas as pd
from datetime import datetime

startTime = datetime.now() # time how long it takes to run the script

############### READ CSV INTO DATAFRAME ###############

df_co = pd.read_csv('x_competitor_buildings_all.csv', encoding='latin1')
df_sf = pd.read_csv('x_competitor_buildings_SF.csv', encoding='latin1')

### Format Addresses

# changes the address column to a string of text, if it is not already
df_co['Address'] = df_co['Address'].astype(str)
df_sf['Street_Address'] = df_sf['Street_Address'].astype(str)

df_co['Address'] = df_co['Address'].str.title()
df_sf['Street_Address'] = df_sf['Street_Address'].str.title()

repl_dict = {
    'street': 'St',
    'avenue': 'Ave',
    'parkway': 'Pkwy',
    'freeway': 'Fwy',
    'circle': 'Cir',
    'boulevard': 'Blvd',
    'court': 'Ct',
    'place': 'Pl',
    'plaza': 'Plz',
    'lane': 'Ln',
    'road': 'Rd',
    'drive': 'Dr',
    'north': 'N',
    'south': 'S',
    'east': 'E',
    'west': 'W',
    'northeast': 'NE',
    'southeast': 'SE',
    'northwest': 'NW',
    'southwest': 'SW'
        }

### Replace keys with values from repl_dict to format address to match database
df_co['Address'] = df_co['Address'].str.lower().replace({k : v for k, v in repl_dict.items()})
df_co['Address'] = df_co['Address'].str.title()
df_co['State'] = df_co['State'].str.upper()

############### SAVE AS A CSV FILE ###############
df_co.to_csv('', index = False, encoding='latin1') # change filename to whatever you want

print('Done!')
print('Script runtime: {}'.format(datetime.now() - startTime))
