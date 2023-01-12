# from dataproc master node shell
gsutil cp gs://joe-test-bucket/*.csv ./

# any data in the master node can be loaded into hdfs like this:
hdfs dfs -mkdir ../../data/
hdfs dfs -mkdir ../../data/strava_files
hdfs dfs -put raw_activities.csv ../../data/strava_files

# now you can display this file 
hdfs dfs -ls ../../data/strava_files