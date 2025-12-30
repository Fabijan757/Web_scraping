from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="books_scrape_dag",
    start_date=datetime(2025, 11, 23),   
    schedule_interval="50 13 * * *",      
    catchup=False,
) as dag:

    run_scraper = BashOperator(
        task_id="run_books_scraper",
        bash_command='python "/opt/airflow/dags/pyhton_web_scraping.py"'
    )

