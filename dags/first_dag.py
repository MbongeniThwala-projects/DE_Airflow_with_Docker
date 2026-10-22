from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator

with DAG(
    dag_id="first_dag",
    schedule_interval="0 6 2 * *",
    start_date=datetime(2021, 1, 1)
    ) as dag:
    op1 = DummyOperator(task_id="task1")
    op2 = DummyOperator(task_id="task2")
    op1 >> op2