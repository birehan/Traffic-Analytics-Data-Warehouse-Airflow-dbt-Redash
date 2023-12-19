from datetime import  timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from sqlalchemy import create_engine
import pandas as pd
import os
import logging

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

def insert_data_into_table():
    # Log the current working directory
    current_working_directory = os.getcwd()
    logging.info(f"Current Working Directory: {current_working_directory}")

    db_connection_url = 'postgresql+psycopg2://airflow:airflow@postgres/airflow'
    engine = create_engine(db_connection_url)

    # Specify the relative path to the CSV file
    csv_file_relative_path = './dags/data/dataset.csv'

    # Get the absolute path
    csv_file_absolute_path = os.path.abspath(csv_file_relative_path)
    logging.info(f"Absolute Path to CSV File: {csv_file_absolute_path}")

    # Read data from CSV file
    df = pd.read_csv(csv_file_relative_path, sep="[,;:]", index_col=False)

    # Insert data into the table
    table_name = 'vehicle_data'
    df.to_sql(table_name, engine, if_exists='replace', index=False)
  


insert_data_task = PythonOperator(
    task_id='insert_data_task',
    python_callable=insert_data_into_table,
    dag=dag,
)



# Set task dependencies
create_airflow_db_task >> create_vehicle_data_table_task >> insert_data_task

if __name__ == "__main__":
    dag.cli()
# /home/babi/Desktop/10academy/Traffic-Analytics-Data-Warehouse-Airflow-dbt-Redash/data/dataset.csv