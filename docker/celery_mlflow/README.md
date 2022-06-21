To start celery, mlflow and all dependencies:

1. Set all variables in the .env file
2. Call docker-compose with the following command from within this folder:

~~~
docker-compose -f ../celery/docker-compose_rabbitmq.yml -f ../mlflow/docker-compose.yml -f docker-compose.override.yml --env-file .env up --build -d
~~~

You can start a corresponding worker from the compose files of the worker directory of this repository and test the deployment via the call_rabbitmq.py script of the celery-mlflow.sample project.
Be aware that you have to add the password and the ip of the broker to the script.
Furthermore, it is sufficient to only execute the *mlflow_add* task and comment the others:

~~~
#app.send_task('app.add',args=(4,4))
#app.send_task('app.add_middle',args=(4,4))
#app.send_task('app.add_long',args=(4,4))
#app.send_task('app.add_extra_long',args=(4,4))

app.send_task('app.mlflow_add',args=(4,4))
~~~
