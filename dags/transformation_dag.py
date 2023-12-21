from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess

default_args = {
    'owner': 'BirehanAnteneh',
    'retries': 3,
    'retry_delay': timedelta(minutes=2),
}

def run_dbt():
    try:
        subprocess.run(['dbt', 'run', '--projects_dir', '/dbt'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running dbt: {e}")

with DAG(dag_id='transform_data', default_args=default_args) as dag:
    dbt_run = PythonOperator(
        task_id='transform',
        python_callable=run_dbt,
        dag=dag
    )
