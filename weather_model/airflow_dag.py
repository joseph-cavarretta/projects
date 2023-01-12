from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator

args = {
    'owner': 'joe-cavarretta',
    'description': 'Use of the DockerOperator',
    'depend_on_past': False,
    'start_date': datetime(2022, 4, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='weather_model',
    default_args=args,
    description='Runs anomaly detection model on Boulder, CO recent weather',
    schedule_interval='15 * * * *'
    #schedule_interval='0 12 * * 0' # run on mondays at noon
) as dag:

    # run model on last 7 days of data
    run_model = BashOperator(
        task_id='run_model',
        bash_command='docker run --rm --volume ~/*/weather_model/src/data:/data weather_model',
        dag=dag,
    )