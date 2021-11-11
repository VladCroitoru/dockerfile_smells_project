FROM python:3.5

RUN pip install airflow[celery,postgres,hive]==1.7.1.3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV AIRFLOW_HOME=/usr/src/app

CMD airflow initdb && airflow webserver -p 80