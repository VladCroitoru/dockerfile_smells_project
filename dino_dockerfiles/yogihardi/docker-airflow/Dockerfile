# VERSION 1.8.2-rc1
# AUTHOR: "yogihardi" 
# DESCRIPTION: Airflow + GCP container
# BUILD: docker build --rm -t yogihardi/docker-airflow .
# SOURCE: https://github.com/yogihardi/docker-airflow

FROM debian:8
MAINTAINER yogihardi

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Airflow
ARG AIRFLOW_VERSION=1.8.2rc1
ARG AIRFLOW_HOME=/usr/local/airflow

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN set -ex \
     && apt-get update && apt-get install -y \
	python3-pip \
	python3-dev \
	build-essential \
	libssl-dev \
	libffi-dev \
	libmysqlclient-dev \
    && easy_install3 -U pip \
    && pip3 install mysqlclient \
    && useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow \
    && pip3 install apache-airflow[gcp_api]==$AIRFLOW_VERSION 

COPY script/entrypoint.sh /entrypoint.sh
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
RUN mkdir ${AIRFLOW_HOME}/configs
RUN mkdir ${AIRFLOW_HOME}/logs
RUN mkdir ${AIRFLOW_HOME}/dags
RUN chown -R airflow: ${AIRFLOW_HOME}

VOLUME ${AIRFLOW_HOME}/dags
VOLUME ${AIRFLOW_HOME}/logs
VOLUME ${AIRFLOW_HOME}/configs

EXPOSE 8080 5555 8793

USER airflow
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
