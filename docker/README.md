This folder contains docker specific files to manage different deployments of celery (and flower), celery workers, and MLflow.


The corresponding docker compose files are grouped in sub-folders:
- celery: contains files to manage celery and flower
- worker: contains files to manage a celery worker
- celery_mflow: contains files to manage celery, flower, and MLflow
- the remaining sub-folders contain utility files for the corresponding services


**Notes**
- Please be aware that the flower service makes use of the celery-mlflow.sample project of this repository to load the same configuration as the sample workers. It is recommended that all workers have to use the same configuration.
- The mflow related files are adapted from https://github.com/sachua/mlflow-docker-compose
- [MLflow is configured to provide proxied artifact storage access](https://www.mlflow.org/docs/latest/tracking.html), such that MinIO credentials do not have to be handled on the client side
- workers use `network_mode: host`, such that they can be started on the same host as celery as well as on remote hosts
