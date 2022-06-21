#Configuration for usage with rabbitmq as broker and long running resource heavy tasks
from os import environ

broker_url = environ['BROKER_URL']
result_backend = environ['RESULT_BACKEND']

task_acks_late = True
worker_prefetch_multiplier = 1
worker_concurrency = 1

task_serializer = "pickle"  
result_serializer = "pickle"
accept_content = ["pickle"]
