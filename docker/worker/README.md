This docker-compose file can manage a simple celery worker.

To build and start the container you have to:

1. Set the password for the broker in the .env file
2. Set the ip of the broker in the .env file
3. Call docker-compose from within this folder

~~~
docker-compose -f docker-compose_<redis or rabbitmq>.yml up -d
~~~
