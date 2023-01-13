from datetime import timedelta, datetime
from airflow import DAG
# docker operator performs equivalent of a run command
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
    schedule_interval='5 * * * *'
    #schedule_interval='0 12 * * 0' # run on mondays at noon
) as dag:

    # run model on last 7 days of data
    run_model = DockerOperator(
        task_id='run_model_container',
        image='weather_model:latest',
        api_version='auto',
        auto_remove=True,
        command="docker run --rm --volume ~/*/weather_model/src/data:/data weather_model",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge"
    )

run_model