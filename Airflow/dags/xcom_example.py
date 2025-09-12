import time

from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'loonycorn'
}

def extract_data(**context):
    data = {"name": "BB", "city": "Vancouver"}
    # push به XCom
    context['ti'].xcom_push(key='user_data', value=data)

def process_data(**context):
    # pull از XCom
    data = context['ti'].xcom_pull(key='user_data', task_ids='extract_task')
    print("Got data:", data)

with DAG(
    dag_id = 'xcom_example', 
    start_date = days_ago(1),
    schedule = None, 
    catchup = False,
    tags = ['xcom', 'python']
)as dag:

    t1 = PythonOperator(
        task_id="extract_task",
        python_callable=extract_data,
        provide_context=True
    )
    t2 = PythonOperator(
        task_id="process_task",
        python_callable=process_data,
        provide_context=True
    )

    t1 >> t2
