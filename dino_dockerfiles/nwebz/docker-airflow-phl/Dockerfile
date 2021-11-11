# Dockerfile for phl-airflow
# find it here: https://github.com/CityOfPhiladelphia/phl-airflow
# use Ubuntu (16.04) base image
FROM ubuntu:16.04

# set maintainer
MAINTAINER Nick Weber <nicholas.weber@phila.gov>

# update local package database
RUN apt-get update

# install phl-airflow dependencies
RUN apt-get install -y build-essential libssl-dev libffi-dev
RUN apt-get install -y python python-pip python-setuptools python-dev python-psycopg2 postgresql-client postgresql-client-common 

# install airflow
RUN pip install "airflow[hive]" cryptography

# clone phl-airflow
RUN apt-get install -y git alien wget libaio1

# grab instant sql-plus instant oracle client/ rename downloaded file and install with alien
RUN wget https://www.dropbox.com/s/ubgeht3m59bhfh1/oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm?dl=0
RUN mv oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm\?dl\=0 oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm
RUN alien -i oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm 

# grab instant basic-lite instant oracle client/ rename downloaded file and install with alien
RUN wget https://www.dropbox.com/s/1yzl0fdnaiw5yqp/oracle-instantclient12.1-basiclite-12.1.0.2.0-1.x86_64.rpm?dl=0
RUN mv oracle-instantclient12.1-basiclite-12.1.0.2.0-1.x86_64.rpm?dl=0 oracle-instantclient12.1-basiclite-12.1.0.2.0-1.x86_64.rpm
RUN alien -i oracle-instantclient12.1-basiclite-12.1.0.2.0-1.x86_64.rpm 

# grab instant oracle-sdk / rename downloaded files and install with alien
RUN wget https://www.dropbox.com/s/uic5vzc9yobttct/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm?dl=0
RUN mv oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm?dl=0 oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm
RUN alien -i oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm

# set oracle environment variables
ENV LD_LIBRARY_PATH /usr/lib/oracle/12.1/client64/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
ENV ORACLE_HOME /usr/lib/oracle/12.1/client64

# clone phl-airflow
#RUN git clone https://github.com/CityOfPhiladelphia/phl-airflow.git ~/home && cd ~/home/phl-airflow

# install dependencies
#RUN pip install -r requirements.txt

# initialize database
#RUN airflow initdb

#RUN airflow webserver -p 8080

USER root
