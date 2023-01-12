from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'joe-cavarretta',
}

with DAG(
    dag_id='get_all_activities',
    default_args=args,
    schedule_interval='0 5 * * *',
    start_date=days_ago(1),
) as dag:

    get_all_activities = BashOperator(
        task_id='get_all_activities',
        bash_command='python3 /<path to file>/get_activities.py',
    )

    get_all_activities

if __name__ == "__main__":
    dag.cli()
