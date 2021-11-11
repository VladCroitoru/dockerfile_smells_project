FROM python:2.7.12

ENV AIRFLOW_HOME=/opt/airflow

# Can be overriden using --build-arg
ARG AIRFLOW_VERSION=1.7.1.3

ADD airflow.cfg /opt/airflow/

WORKDIR /opt/airflow

# Install airflow and airflow dependencies
RUN pip install airflow==$AIRFLOW_VERSION 
RUN pip install airflow[hive]==$AIRFLOW_VERSION

RUN airflow initdb

CMD airflow webserver -p 8080
