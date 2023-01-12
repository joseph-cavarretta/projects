from google.cloud import bigquery

PROJECT_ID = "joe-test-project-373803"
TARGET_TABLE_ID = f"{PROJECT_ID}.strava.types"

def create_dim_table(PROJECT_ID, TARGET_TABLE_ID):
    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig(
        destination=TARGET_TABLE_ID,
        write_disposition='WRITE_TRUNCATE')

    sql = f"SELECT type FROM `{PROJECT_ID}.strava.raw_activities`;"

    query_job = client.query(sql, job_config=job_config)
    
    try:
        query_job.result()
        print("Query success")
    except Exception as exception:
            print(exception)

if __name__ == '__main__':
    create_dim_table(PROJECT_ID, TARGET_TABLE_ID)
