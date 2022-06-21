from celery import Celery
from os import environ

from worker.app import mlflow_add
from utility.utility import Parameters

broker_pw = 'test'
broker_ip = 'localhost'

environ.setdefault('CELERY_CONFIG_MODULE', 'config.celery_config_rabbitmq_long')
environ.setdefault('BROKER_URL', 'amqp://admin:{}@{}:5672//'.format(broker_pw, broker_ip))
environ.setdefault('RESULT_BACKEND', 'redis://:{}@{}:6380/0'.format(broker_pw, broker_ip))

app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')

app.send_task('app.add',args=(4,4))
#app.send_task('app.add_middle',args=(4,4))
#app.send_task('app.add_long',args=(4,4))
#app.send_task('app.add_extra_long',args=(4,4))

mlflow_add.delay(Parameters(4,4))
