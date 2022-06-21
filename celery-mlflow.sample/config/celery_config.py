#Simple configuration
from os import environ

broker_url = environ['BROKER_URL']
result_backend = environ['RESULT_BACKEND']

task_serializer = "pickle"  
result_serializer = "pickle"
accept_content = ["pickle"]