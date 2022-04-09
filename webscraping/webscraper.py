import pandas as pd
import urllib
from bs4 import BeautifulSoup as soup
from datetime import datetime

###
startTime = datetime.now()
###

## ENTER URL OF PAGE TO SCRAPE
url = 'insert URL here'

## OPEN URL
source = urllib.request.urlopen(url).read()

## CREATES A DATA STRUCTURE OF PARSED HTML
page_soup = soup(source, 'html.parser')

## TABLES IS A NESTED DF, 0th INDEX IS DF OF COLUMN NAMES.
## READ HTML INTO DF
tables = pd.read_html(url)

## INDEX 1 OF TABLES HOLD THE TABLE VALUES
table = tables[1]

## USE FIND() ON PAGE_SOUP OBJECT TO LOCATE NUMBER OF PAGES INFO
res = page_soup.find("div", {"class": "location-pagination"}).text

## PARSES OUT HOW MANY PAGES WE NEED TO ITERATE THROUGH
page_total = int(res.split('/')[1].split('\xa0')[0])


## LOOP THROUGH OUR RANGE OF PAGES
for i in range(2,page_total+1):
    # update url with current page number
    new_url = url + f'&page={i}'

    # read_html on current page and set nested df to temp variable
    temp_tables = pd.read_html(new_url)

    # append values of nested df (index 1) to our table of all values
    table = table.append(temp_tables[1])
    print(i)

## SET COLUMN NAMES
column_names = ['Site Type',
                'Country',
                'City, State',
                'Building Name',
                'Address',
                'Zip Code']

table.columns = column_names

table.to_csv('', index = False)

print('\nFile Saved!')
print('Script runtime: {}'.format(datetime.now() - startTime))
