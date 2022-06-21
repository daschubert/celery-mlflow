This docker-compose file can manage a simple celery and flower setup using redis or rabbitmq as broker and redis as result backend.

To build and start the containers you have to:

1. Set the password for the broker and backend via an environment variable
2. Set the BROKER_IP to reference the redis or rabbitmq container
2. Call docker-compose from within this folder

~~~
export BROKER_PW=<your_pw>
export BROKER_IP=<redis or rabbitmq>
docker-compose -f docker-compose-<redis or rabbitmq>.yml up -d
~~~

You can start a corresponding worker from the compose files of the worker directory of this repository and test the deployment via the call_<broker>.py scripts of the celery-mlflow.sample project.
Be aware that you have to:
- adapt the config module loaded in app.py to match your broker

~~~
environ.setdefault('CELERY_CONFIG_MODULE', 'config.<python module in config package that matches your broker>')
e.g.: environ.setdefault('CELERY_CONFIG_MODULE', 'config.celery_config_rabbitmq_long')
~~~

- and add the password and the ip of the broker to the script.
