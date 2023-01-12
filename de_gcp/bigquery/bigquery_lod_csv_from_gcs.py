from google.cloud import bigquery

DATE = "2023-01-06"
PROJECT_ID = "joe-test-project-373803"
TABLE_ID = f"{PROJECT_ID}.strava.raw_activities"
GCS_URI = f"gs://{PROJECT_ID}/raw_activities_{DATE}.csv"

def load_gcs_to_bigquery_snapshot_data(GCS_URI, TABLE_ID, table_schema):
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        schema = table_schema,
        source_format = bigquery.SourceFormat.CSV,
        write_disposition = 'WRITE_TRUNCATE'
        )

    load_job = client.load_table_from_uri(
        GCS_URI, TABLE_ID, job_config=job_config
    )
    load_job.result()
    table = client.get_table(TABLE_ID)

    print(f"Loaded {table.num_rows} rows to table {TABLE_ID}")

bigquery_table_schema = [
    bigquery.SchemaField("id", "INTEGER"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("start_date_local", "TIMESTAMP")
]

if __name__ == '__main__':
    load_gcs_to_bigquery_snapshot_data(GCS_URI, TABLE_ID, bigquery_table_schema)
