FROM python:3.9-slim-buster

ADD ./ /celery-mlflow.sample
WORKDIR /celery-mlflow.sample
RUN pip install -r requirements_worker.txt

CMD ["echo", "hello"]
