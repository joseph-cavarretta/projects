bucket_name=joe-test-bucket-373803
date=20230106
gcloud sql export csv mysql-instance-source \
gs://$bucket_name/mysql_export/strava/$date/activities.csv \
--database=strava \
--offload \
--query='SELECT * FROM activities;'

# to run: sh export_cloudsql_to_gcs.sh