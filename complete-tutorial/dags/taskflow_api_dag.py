from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    'owner': 'rishabh',
    'retries': 5,
    'retry_delay': timedelta(seconds=30)
}


@dag(dag_id='taskflow_api_dag',
     default_args=default_args,
     start_date=datetime(2023, 7, 15),
     schedule_interval='@daily',
     catchup=False)
def hello_world_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Rishabh',
            'last_name': 'Goel'
        }

    @task()
    def get_age():
        return 27

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name} "
              f"and I am {age} years old!")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'], age=age)


greet_dag = hello_world_etl()
