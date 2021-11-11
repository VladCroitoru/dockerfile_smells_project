# VERSION 1.8.2rc1
# AUTHOR: G. Ghez
# DESCRIPTION: Python 3.5 Prod Airflow container
# BUILD: docker build --rm -t gghez/docker-airflow .
# SOURCE: https://github.com/gghez/docker-airflow

FROM python:3.5-slim
MAINTAINER gghez

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

RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y --no-install-recommends python3-dev libkrb5-dev libsasl2-dev libssl-dev libffi-dev build-essential libblas-dev liblapack-dev libpq-dev git python-requests curl netcat locales

RUN sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen
RUN locale-gen
RUN update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
RUN useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow

RUN pip install Cython pytz pyOpenSSL ndg-httpsclient pyasn1 flask_bcrypt
RUN pip install apache-airflow[crypto,celery,postgres,hive,hdfs,jdbc]==$AIRFLOW_VERSION
RUN pip install celery[redis]

# Remove airflow example files
RUN rm -fr /usr/local/lib/python3.5/site-packages/airflow/example_dags/

# Airflow tools for bash commands
RUN apt-get install -y --no-install-recommends rsync openssh-client sshpass

RUN apt-get clean
RUN rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base

COPY script/entrypoint.sh /entrypoint.sh
COPY script/init_meta_db.py /init_meta_db.py
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

RUN chmod +x /entrypoint.sh
RUN chown -R airflow: ${AIRFLOW_HOME}

EXPOSE 8080 5555 8793

USER airflow
WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
