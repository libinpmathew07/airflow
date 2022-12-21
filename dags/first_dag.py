from airflow.models import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def printnm():
    print("printing name")
with DAG(dag_id="first_dag",schedule_interval="@daily",start_date=datetime(year=2022,month=11,day=27),catchup=False) as dag:
    task_one=PythonOperator(task_id='print_name',python_callable=printnm)