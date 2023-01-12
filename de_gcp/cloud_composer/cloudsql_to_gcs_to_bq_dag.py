from airflow import DAG
from airflow.contrib.operators.gcp_sql_operator import CloudSqlInstanceExportOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'joe-cavarretta',
}

GCP_PROJECT_ID = 'joe-test-project-373803'
INSTANCE_NAME = '<mysql-instance>'
EXPORT_URI = 'gs://joe-test-bucket'
SQL_QUERY = 'SELECT * FROM strava.activities'

export_body = {
    "exportContext": {
        "fileType": "csv",
        "uri": EXPORT_URI,
        "csvExportOptions":{
            "selectQuery": SQL_QUERY
        }
    }
    
}

with DAG(
    dag_id='cloudsql_to_gcs_to_bq',
    default_args=args,
    schedule_interval='0 5 * * *',
    start_date=days_ago(1),
) as dag:

    cloudsql_to_gcs = CloudSqlInstanceExportOperator(
        task_id='cloudsql_to_gcs',
        project_id=GCP_PROJECT_ID, 
        body=export_body, 
        instance=INSTANCE_NAME
    )

    gcs_to_bq = GoogleCloudStorageToBigQueryOperator(
    task_id                             = "gcs_to_bq",
    bucket                              = 'joe-test-bucket',
    source_objects                      = ['mysql_export/from_composer/raw_activities.csv'],
    destination_project_dataset_table   = 'strava.raw_activities',
    schema_fields=[
        {'name': 'id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'start_date_local', 'type': 'TIMESTAMP', 'mode': 'NULLABLE'},
        {'name': 'type', 'type': 'STRING', 'mode': 'NULLABLE'}
    ],
    write_disposition='WRITE_TRUNCATE'
    )

    bq_to_bq  = BigQueryOperator(
        task_id                     = "bq_to_bq",
        sql                         = "SELECT type, count(*) as count FROM `strava.raw_activities` GROUP BY type",
        destination_dataset_table   = 'strava.temp_activities_count',
        write_disposition           = 'WRITE_TRUNCATE',
        create_disposition          = 'CREATE_IF_NEEDED',
        priority                    = 'BATCH',
        use_legacy_sql              = False
    )

    cloudsql_to_gcs >> gcs_to_bq >> bq_to_bq

if __name__ == "__main__":
    dag.cli()
