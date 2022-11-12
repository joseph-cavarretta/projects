-- to run: mysql -u root -p -e "source load_data.sql"

LOAD DATA INFILE 'raw_activities.csv'
INTO TABLE `strava_staging`.`raw_data`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'processed_activitites.csv'
INTO TABLE `strava_staging`.`processed_data`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;