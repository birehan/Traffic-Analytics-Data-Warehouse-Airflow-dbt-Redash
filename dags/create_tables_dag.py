from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from sqlalchemy import create_engine
import os

default_args = {
    'owner': 'BirehanAnteneh',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

dag = DAG(
    'create_vehicle_tables',
    default_args=default_args,
    description='A simple DAG to create a database and two tables in the PostgreSQL database',
    schedule_interval=None,  # You can set the schedule_interval as needed
)

# Function to execute SQL script
def execute_sql_script(script_path):
    # Connection details
    db_connection_url = 'postgresql+psycopg2://airflow:airflow@postgres/airflow'

    # Create SQLAlchemy engine and connect to the database
    engine = create_engine(db_connection_url)

    # Read SQL script content
    with open(script_path, 'r') as script_file:
        script_content = script_file.read()

    # Execute the SQL script
    with engine.connect() as connection:
        connection.execute(script_content)

# Task to create the "airflow" database
create_airflow_db_task = PythonOperator(
    task_id='create_airflow_db_task',
    python_callable=execute_sql_script,
    op_kwargs={'script_path': './dags/sql/create_db.sql'},
    dag=dag,
)

# Task to create the vehicle_data table
create_vehicle_data_table_task = PythonOperator(
    task_id='create_vehicle_data_table_task',
    python_callable=execute_sql_script,
    op_kwargs={'script_path': './dags/sql/create_vehicle_table.sql'},
    dag=dag,
)

# Task to create the detailed_vehicle_info table
create_detailed_vehicle_info_table_task = PythonOperator(
    task_id='create_detailed_vehicle_info_table_task',
    python_callable=execute_sql_script,
    op_kwargs={'script_path': './dags/sql/create_vehicle_detail_table.sql'},
    dag=dag,
)

# Set task dependencies
create_airflow_db_task >> create_vehicle_data_table_task
create_vehicle_data_table_task >> create_detailed_vehicle_info_table_task

if __name__ == "__main__":
    dag.cli()
