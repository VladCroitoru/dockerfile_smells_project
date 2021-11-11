FROM python:3.9.6

RUN mkdir /meetup
WORKDIR /meetup

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt-get install -y vim less

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install google-cloud-storage
RUN pip install google-cloud-bigquery
