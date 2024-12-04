from airflow import DAG
import datetime
from airflow.operators.empty import EmptyOperator
from airflow.decorators import dag

# way 1 to declare DAG
with DAG(
        dag_id="hands_on_dag",
        start_date=datetime.datetime(2021, 1, 1),
        schedule="@daily",
):
    EmptyOperator(task_id="task")


#way 2 to declare DAG
my_dag = DAG(
     dag_id="my_dag_name",
     start_date=datetime.datetime(2021, 1, 1),
     schedule="@daily",
 )
EmptyOperator(task_id="task", dag=my_dag)

#way 3 to declare DAG
@dag(start_date=datetime.datetime(2021, 1, 1), schedule="@daily")
def generate_dag():
    EmptyOperator(task_id="task")


generate_dag()



