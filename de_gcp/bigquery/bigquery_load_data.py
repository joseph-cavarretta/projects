from google.cloud import bigquery

PROJECT_ID = "joe-test-project-373803"
GCS_URI = f"gs://{PROJECT_ID}/*.json"
TABLE_ID = f"{PROJECT_ID}.strava.activities"

client = bigquery.Client()

bigquery_table_schema = [
    bigquery.SchemaField("id", "INTEGER"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("start_date_local", "TIMESTAMP")
]

def load_gcs_to_bigquery_event_data(GCS_URI, TABLE_ID, table_schema):
    job_config = bigquery.LoadJobConfig(
        schema=table_schema,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition='WRITE_APPEND'
        )

    load_job = client.load_table_from_uri(
        GCS_URI, TABLE_ID, job_config=job_config
    )

    load_job.result()
    table = client.get_table(TABLE_ID)

    print(f"Loaded {table.num_rows} rows to table {TABLE_ID}")


if __name__ == '__main__':
    load_gcs_to_bigquery_event_data(GCS_URI, TABLE_ID, bigquery_table_schema)
