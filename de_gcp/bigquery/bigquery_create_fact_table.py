import sys
from google.cloud import bigquery


PROJECT_ID = "joe-test-project-373803"
TARGET_TABLE_ID = f"{PROJECT_ID}.strava.raw_activities"

def create_fact_table(PROJECT_ID, TARGET_TABLE_ID):
    load_date = sys.argv[1] # date format : yyyy-mm-dd
    print("\nLoad date: ", load_date)

    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig(
    destination=TARGET_TABLE_ID,
    write_disposition='WRITE_APPEND')

    sql = f"""SELECT id, DATE(start_date_local), type
          FROM {PROJECT_ID}.strava.raw_activities;"""

    query_job = client.query(sql, job_config=job_config)

    try:
        query_job.result()
        print("Query success")
    except Exception as exception:
            print(exception)

if __name__ == '__main__':
    create_fact_table(PROJECT_ID, TARGET_TABLE_ID)
