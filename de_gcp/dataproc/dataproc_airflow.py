from airflow.providers.google.cloud.operators.dataproc import (
    DataprocCreateClusterOperator,
    DataprocDeleteClusterOperator,
    DataprocSubmitJobOperator
)

PROJECT_ID = 'joe-test-project-737803'
REGION = 'uscentral1'
CLUSTER_NAME = 'ephemeral-spark-cluster-{{ ds_nodash }}'
cluster_config_json = {
    "worker_config": {
        "num_instances": 2
    }
}
create_cluster = DataprocCreateClusterOperator(
    task_id="create_cluster",
    project_id=PROJECT_ID,
    cluster_config=cluster_config_json,
    region=REGION,
    cluser_name=CLUSTER_NAME,
    idle_delete_ttl=600 # delete cluster after this many seconds
)

PYSPARK_URI = 'gs://joe-test-bucket/.../pyspark_gcs_to_bq.py'
PYSPARK_JOB = {
    "reference": {'project_id': PROJECT_ID},
    "placement": {'cluster_name': CLUSTER_NAME},
    "pyspark_job": {"main_python_file_uri": PYSPARK_URI,
    "jar_file_uris": ['gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar']
    }
}
pyspark_task = DataprocSubmitJobOperator(
    task_id='pyspark_task',
    job=PYSPARK_JOB,
    location=REGION,
    project_id=PROJECT_ID
)
delete_cluster = DataprocDeleteClusterOperator(
    task_id='delete_cluster',
    project_id=PROJECT_ID,
    cluster_name=CLUSTER_NAME,
    region=REGION
)

create_cluster >> pyspark_task >> delete_cluster