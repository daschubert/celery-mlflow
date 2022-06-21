from os import environ
from celery import Celery
import time

from utility.utility import Parameters

MLFLOW_IP='localhost'

environ.setdefault('CELERY_CONFIG_MODULE', 'config.celery_config_rabbitmq_long')

app = Celery()
app.config_from_envvar('CELERY_CONFIG_MODULE')

@app.task(name='app.add')
def add(x, y):
    return x + y

@app.task(name='app.add_middle')    
def add_middle(x,y):
    time.sleep(30) #30 seconds
    return x + y 

@app.task(name='app.add_long')
def add_long(x, y):
    time.sleep(3900) #1 hour 5 minutes
    return x + y

@app.task(name='app.add_extra_long')
def add_extra_long(x, y):
    time.sleep(46800) #13 hours
    return x + y

# Logs to MLFlow and uses complex datatype as input (pickle is used as serializer, cf. config files)
@app.task(name='app.mlflow_add')
def mlflow_add(par: Parameters):
    import mlflow
    import os
    result = None
    
    mlflow.set_tracking_uri('http://{}:5000'.format(MLFLOW_IP))
    mlflow.set_experiment("Adding")
            
    with mlflow.start_run():
        mlflow.log_param('x', par.x)
        mlflow.log_param('y', par.y)
        
        result = par.x + par.y
    
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        with open("outputs/test.txt", "w") as f:
            f.write("{} + {} = {}".format(par.x, par.y, result))
        
        mlflow.log_artifacts("outputs")
        
    return result