This docker-compose file can manage a simple celery worker.

To build and start the container you have to:

1. Set the password for the broker via an environment variable
2. Set the ip of the broker via an environment variable
3. Call docker-compose from within this folder

~~~
export BROKER_PW=<your_pw>
export BROKER_IP=<ip of your broker and backend>
docker-compose -f docker-compose_<redis or rabbitmq>.yml up -d
~~~
