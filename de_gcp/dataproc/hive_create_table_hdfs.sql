CREATE EXTERNAL TABLE raw_activities(
    id INTEGER,
    start_date_local DATE,
    type STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
location 'data/strava_files'
TBLPROPERTIES ("skip.header.line.count"="1")
;
