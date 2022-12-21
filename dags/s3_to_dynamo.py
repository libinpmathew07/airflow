from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def first():
    print('myfrist dag and task')

def second():
    print('second task')
with DAG(
    dag_id='s3_to_dynamo',
    schedule_interval='@daily',
    start_date=datetime(year=2022,month=11,day=25),
    catchup=False)as dag:
    demo_task=PythonOperator(task_id='demo1',python_callable=first)
    demo_task1=PythonOperator(task_id='demo2',python_callable=second)
demo_task>>demo_task1
