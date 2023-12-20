# Traffic-Analytics-Data-Warehouse-Airflow-dbt-Redash

## Overview

This project focuses on creating a scalable data warehouse for a city traffic department, utilizing swarm UAVs (drones) to collect traffic data. The data is intended for improving traffic flow and undisclosed projects. The tech stack comprises MySQL, DBT, and Airflow, following the Extract Load Transform (ELT) framework.

![Tech Stack Flow](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*e33d2qsI15lKO5a--O8Ocg.png?raw=true)

## Project Structure

The project structure includes:

- **data:** Raw and cleaned datasets' CSV files.
- **dags:** Airflow DAGs for task orchestration.
- **notebooks:** Jupyter notebook for Explanatory Data Analysis (EDA).
- **screenshots:** Visual representations of the project, including tech stack flow, path for track ID, and speed comparisons.
- **scripts:** Python utility scripts.
- **traffic_dbt:** dbt (Data Build Tool) files and configurations.
- **docker-compose.yaml:** YAML file for Docker Compose, facilitating the setup of Airflow and Docker.

# Airflow Data Loading with Docker

This repository contains the necessary files to set up a Dockerized Airflow environment for data loading into PostgreSQL.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/airflow-data-loading.git
   cd airflow-data-loading
   ```

2. **Configure Environment Variables (Optional):**

   If needed, you can set environment variables by creating a `.env` file in the project root. Adjust variables as necessary.

   Example `.env` file:

   ```env
   AIRFLOW_UID=1001
   AIRFLOW_IMAGE_NAME=apache/airflow:2.8.0
   _PIP_ADDITIONAL_REQUIREMENTS=your_additional_requirements.txt
   ```

3. **Build and Run Airflow Services:**

   ```bash
   docker-compose up --build
   ```

4. **Access Airflow Web Interface:**

   Once the services are running, access the Airflow web interface at [http://localhost:8080](http://localhost:8080).

5. **Stop Airflow Services:**

   When you're done, stop the Airflow services:

   ```bash
   docker-compose down
   ```

## DAG Information

- The Airflow DAG `create_vehicle_tables` is designed to create a PostgreSQL database, tables, and load data from a CSV file.
- Customize the DAG or SQL scripts in the `dags` and `dags/sql` directories as needed.

## Additional Notes

- Make sure to adjust file paths, database connection details, and other configurations in the DAG and SQL scripts to suit your environment.

## Troubleshooting

- If you encounter any issues, refer to the [Troubleshooting](#troubleshooting) section in the README.

## License

This project is licensed under the [Apache License, Version 2.0](LICENSE).
