# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:22:33 2021

@author: joe.cavarretta
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

############### OPEN CSV & READ INTO DATAFRAME ###############
file_name = 'analysis'
final_file_name = file_name + '.xlsx'
df = pd.read_excel(final_file_name, sheet_name = 'all_sites')

## Get average price and sort ascending
avg_prices = df.groupby('Supplier_Account')['1G','500Mb','100Mb','50Mb'].mean().sort_values(by='Supplier_Account', ascending = True).reset_index()

## Generate count of buildings for each Supplier Account
count_buildings = df.groupby('Supplier_Account')['Building_Name'].count().reset_index()

## Merge count of buildings into dataframes
avg_prices = avg_prices.merge(count_buildings)
avg_prices.rename(columns={'Bldg_Name': 'Count of Bldgs'}, inplace = True)

## Normalize number of buildings for plot bubble sizes to not be too big or too small
avg_prices['Count of Buildings Reduce'] = np.where(avg_prices['Count of Buildings'] > 1,
                                                   avg_prices['Count of Buildings']/5,
                                                   avg_prices['Count of Buildings']+5)

### Create individual plot datasets for overall pricing
plt_1G = avg_prices[['Supplier_Account','1G','Count of Buildings', 'Count of Buildings Reduce']].sort_values(by = '1G', ascending = True)
plt_500Mb = avg_prices[['Supplier_Account','500Mb','Count of Buildings', 'Count of Buildings Reduce']].sort_values(by = '500Mb', ascending = True)
plt_100Mb = avg_prices[['Supplier_Account','100Mb','Count of Buildings', 'Count of Buildings Reduce']].sort_values(by = '100Mb', ascending = True)
plt_50Mb = avg_prices[['Supplier_Account','50Mb','Count of Buildings', 'Count of Buildings Reduce']].sort_values(by = '50Mb', ascending = True)

### Create plot
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(14, 8))

### Set Colors
colors_1G = np.where(plt_1G['Supplier_Account'].eq('company name'),'orangered','royalblue')
colors_500Mb = np.where(plt_500Mb['Supplier_Account'].eq('company name'),'orangered','royalblue')
colors_100Mb = np.where(plt_100Mb['Supplier_Account'].eq('company name'),'orangered','royalblue')
colors_50Mb = np.where(plt_50Mb['Supplier_Account'].eq('company name'),'orangered','royalblue')

# suptitle function adds a centered title to the full canvas.
fig.suptitle('company name vs Competitors Pricing', fontsize=14)

# Top Left Subplot
ax[0,0].scatter(plt_1G['1G'], plt_1G['Supplier_Account'], s = plt_1G['Count of Buildings Reduce'], alpha = 0.6, c = colors_1G)
ax[0,0].set_title("1G")

# Top Right Subplot
ax[0,1].scatter(plt_500Mb['500Mb'], plt_500Mb['Supplier_Account'], s = plt_500Mb['Count of Buildings Reduce'], alpha = 0.6, c = colors_500Mb)
ax[0,1].set_title("500Mb")

# Bottom Left Subplot
ax[1,0].scatter(plt_100Mb['100Mb'], plt_100Mb['Supplier_Account'], s = plt_100Mb['Count of Buildings Reduce'], alpha = 0.6, c = colors_100Mb)
ax[1,0].set_title("100Mb")

# Bottom Right Subplot
ax[1,1].scatter(plt_50Mb['50Mb'], plt_50Mb['Supplier_Account'], s = plt_50Mb['Count of Buildings Reduce'], alpha = 0.6, c = colors_50Mb)
ax[1,1].set_title("50Mb")

## Change x-axis label to show $ currency sign
plt.tight_layout()
plt.show()

##########################################################################################################################################################

### Create Dataframes for Data Center vs Enterprise by each bandwidth
Enterprise_df = df.loc[lambda df: df['Building Roll Up'] == 'Enterprise']
DC_df = df.loc[lambda df: df['Building Roll Up'] == 'Data Center']

E_avg_prices = Enterprise_df.groupby('Supplier_Account')['1G','500Mb','100Mb','50Mb'].mean().sort_values(by='Supplier_Account', ascending = True).reset_index()
DC_avg_prices = DC_df.groupby('Supplier_Account')['1G','500Mb','100Mb','50Mb'].mean().sort_values(by='Supplier_Account', ascending = True).reset_index()

count_E_buildings = Enterprise_df.groupby('Supplier_Account')['Building__r.Name'].count().reset_index()
count_DC_buildings = DC_df.groupby('Supplier_Account')['Building__r.Name'].count().reset_index()

###
E_avg_prices = E_avg_prices.merge(count_E_buildings)
E_avg_prices.rename(columns={'Bldg_Name': 'Count of Buildings'}, inplace = True)
###
DC_avg_prices = DC_avg_prices.merge(count_DC_buildings)
DC_avg_prices.rename(columns={'Bldg_Name': 'Count of Buildings'}, inplace = True)

E_avg_prices['Count of Buildings Reduce'] = np.where(E_avg_prices['Count of Buildings'] > 1,
                                                     E_avg_prices['Count of Buildings']/5,
                                                     E_avg_prices['Count of Buildings']+5)

DC_avg_prices['Count of Buildings Reduce'] = np.where(DC_avg_prices['Count of Buildings'] > 1,
                                                      DC_avg_prices['Count of Buildings']+50,
                                                      DC_avg_prices['Count of Buildings']+0)

### Create plot datsets for DC vs Enterprise pricing
plt_1G_E = E_avg_prices[['Supplier_Account','1G','Count of Buildings','Count of Buildings Reduce']].sort_values(by = '1G', ascending = True)
plt_500Mb_E = E_avg_prices[['Supplier_Account','500Mb','Count of Buildings','Count of Buildings Reduce']].sort_values(by = '500Mb', ascending = True)
plt_100Mb_E = E_avg_prices[['Supplier_Account','100Mb','Count of Buildings','Count of Buildings Reduce']].sort_values(by = '100Mb', ascending = True)
plt_50Mb_E = E_avg_prices[['Supplier_Account','50Mb','Count of Buildings','Count of Buildings Reduce']].sort_values(by = '50Mb', ascending = True)

plt_1G_DC = DC_avg_prices[['Supplier_Account','1G','Count of Buildings','Count of Buildings Reduce']].sort_values(by = '1G', ascending = True)
plt_500Mb_DC = DC_avg_prices[['Supplier_Account','500Mb','Count of Buildings','Count of Buildings Reduce']].sort_values(by = '500Mb', ascending = True)
plt_100Mb_DC = DC_avg_prices[['Supplier_Account','100Mb','Count of Buildings','Count of Buildings Reduce']].sort_values(by = '100Mb', ascending = True)
plt_50Mb_DC = DC_avg_prices[['Supplier_Account','50Mb','Count of Buildings','Count of Buildings Reduce']].sort_values(by = '50Mb', ascending = True)

### Create plot for Data Center vs Enterprise
fig1, ax1 = plt.subplots(nrows = 2, ncols = 2, figsize = (14, 8))
fig1.suptitle('DC vs Enterprise Pricing', fontsize=14)

# Top Left Subplot
ax1[0,0].scatter(plt_1G_E['1G'], plt_1G_E['Supplier_Account'], s = plt_1G_E['Count of Buildings Reduce'], alpha = 0.6, c = 'royalblue')
ax1[0,0].scatter(plt_1G_DC['1G'], plt_1G_DC['Supplier_Account'], s = plt_1G_DC['Count of Buildings Reduce'], c = 'orangered', alpha = 0.6, marker = '^')
ax1[0,0].set_title("1G")


# Top Right Subplot
ax1[0,1].scatter(plt_500Mb_E['500Mb'], plt_500Mb_E['Supplier_Account'],
                 s = plt_500Mb_E['Count of Buildings Reduce'],
                 c = 'royalblue', alpha = 0.6)

ax1[0,1].scatter(plt_500Mb_DC['500Mb'], plt_500Mb_DC['Supplier_Account'],
                 s = plt_500Mb_DC['Count of Buildings Reduce'],
                 c = 'orangered', alpha = 0.6, marker = '^')

ax1[0,1].set_title("500Mb")

# Bottom Left Subplot
ax1[1,0].scatter(plt_100Mb_E['100Mb'], plt_100Mb_E['Supplier_Account'],
                 s = plt_100Mb_E['Count of Buildings Reduce'],
                 c = 'royalblue', alpha = 0.6)

ax1[1,0].scatter(plt_100Mb_DC['100Mb'], plt_100Mb_DC['Supplier_Account'],
                 s = plt_100Mb_DC['Count of Buildings Reduce'],
                 c = 'orangered', alpha = 0.6, marker = '^')

ax1[1,0].set_title("100Mb")

# Bottom Right Subplot
ax1[1,1].scatter(plt_50Mb_E['50Mb'], plt_50Mb_E['Supplier_Account'],
                 s = plt_50Mb_E['Count of Buildings Reduce'],
                 c = 'royalblue',alpha = 0.6)

ax1[1,1].scatter(plt_50Mb_DC['50Mb'], plt_50Mb_DC['Supplier_Account'],
                 s = plt_50Mb_DC['Count of Buildings Reduce'],
                 c = 'orangered', alpha = 0.6, marker = '^')

ax1[1,1].set_title("50Mb")

## Change x-axis label to show $ currency sign
plt.tight_layout()
plt.show()
