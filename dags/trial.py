from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from sqlalchemy import create_engine, Column, String, MetaData, Table

# Define the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'create_users_table',
    default_args=default_args,
    description='A simple DAG to create a users table in the PostgreSQL database',
    schedule_interval=None,  # You can set the schedule_interval as needed
)

# Function to create the users table in the PostgreSQL database
def create_users_table():
    # Connection details
    db_connection_url = 'postgresql+psycopg2://airflow:airflow@postgres/airflow'

    # Create SQLAlchemy engine and connect to the database
    engine = create_engine(db_connection_url)
    connection = engine.connect()

    # Define the users table
    metadata = MetaData()
    users_table = Table(
        'users',
        metadata,
        Column('id', String, primary_key=True),
        Column('name', String),
        Column('email', String),
    )

    # Create the table
    metadata.create_all(engine)

    # Close the database connection
    connection.close()

# Task to create the users table
create_users_table_task = PythonOperator(
    task_id='create_users_table_task',
    python_callable=create_users_table,
    dag=dag,
)

# Set task dependencies if any
# create_users_table_task >> task2 >> task3

if __name__ == "__main__":
    dag.cli()
