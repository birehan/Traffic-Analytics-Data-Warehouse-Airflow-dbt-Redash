from datetime import timedelta
import logging
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from sqlalchemy import create_engine
import pandas as pd
import psycopg2

# sys.path.append(os.path.abspath(os.path.join('../scripts')))
from utils import run_sql_query, populate_dataframe_to_database


# Define default DAG arguments
default_args = {
    'owner': 'Birehan Anteneh',
    'depends_on_past': False,
    'email_on_failure': False,
    # 'email': ['birehananteneh4@gmail.com'],

    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}

connection_params = {
    "host": "localhost",
    "user": "airflow",
    "password": "airflow",
    "port": "5432",
    "database": "airflow"  # Change to your desired database name
}

vehicle_data_table_name = "vehicle_data"
vehicle_trajectory_table_name = "vehicle_trajectory"


# Create an Airflow DAG
dag = DAG(
    'create_vehicle_tables',
    default_args=default_args,
    description='A DAG to create a database and tables, and load data into PostgreSQL',
    schedule_interval=None,  # Set the schedule_interval as needed
)

def execute_sql_script(script_path):
    """
    Executes a SQL script.

    Args:
        script_path (str): Path to the SQL script file.
        
    """
    # db_connection_url = 'postgresql+psycopg2://airflow:airflow@postgres/airflow'
    # engine = create_engine(db_connection_url)


    # # Read SQL script content
    # with open(script_path, 'r') as script_file:
    #     script_content = script_file.read()
    
    #  # Execute the SQL script
    # with engine.connect() as connection:
    #     connection.execute(script_content)




    # Read SQL script content
    with open(script_path, 'r') as script_file:
        script_content = script_file.read()
    
    logging.info(script_content)


    connection = psycopg2.connect(**connection_params)

    # Create a cursor
    cursor = connection.cursor()

    # Execute the SQL query
    cursor.execute(script_content)

    # Commit the transaction
    connection.commit()
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    run_sql_query(connection_params, script_content)



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

# Task to create the trajectory table
create_trajectory_data_table_task = PythonOperator(
    task_id='create_trajectory_data_table_task',
    python_callable=execute_sql_script,
    op_kwargs={'script_path': './dags/sql/create_trajectory_table.sql'},
    dag=dag,
)

# def insert_data_into_table():
#     """
#     Reads data from a CSV file and inserts it into the 'vehicle_data' table in PostgreSQL.
#     """

#     db_connection_url = 'postgresql+psycopg2://airflow:airflow@postgres/airflow'
#     engine = create_engine(db_connection_url)

#     # Specify the relative path to the CSV file
#     csv_file_relative_path = './dags/data/dataset.csv'

#     # Read data from CSV file
#     df = pd.read_csv(csv_file_relative_path, sep="[,;:]", index_col=False)

#     # Insert data into the table
#     table_name = 'vehicle_data'
#     df.to_sql(table_name, engine, if_exists='replace', index=False)
  
# insert_data_task = PythonOperator(
#     task_id='insert_data_task',
#     python_callable=insert_data_into_table,
#     dag=dag,
# )

# Set task dependencies
create_airflow_db_task >> create_vehicle_data_table_task >> create_trajectory_data_table_task

if __name__ == "__main__":
    dag.cli()

