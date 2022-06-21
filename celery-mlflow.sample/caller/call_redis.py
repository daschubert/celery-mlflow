from celery import Celery
from os import environ

broker_pw = ''
broker_ip = 'localhost'
broker_port= '6380'

environ.setdefault('CELERY_CONFIG_MODULE', 'config.celery_config_redis_long')
environ.setdefault('BROKER_URL', 'redis://:{}@{}:{}/0'.format(broker_pw, broker_ip, broker_port))
environ.setdefault('RESULT_BACKEND', 'redis://:{}@{}:{}/0'.format(broker_pw, broker_ip, broker_port))

app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')

app.send_task('app.add',args=(4,4))
app.send_task('app.add_middle',args=(4,4))
app.send_task('app.add_long',args=(4,4))
app.send_task('app.add_extra_long',args=(4,4))

app.send_task('app.mlflow_add',args=(4,4))