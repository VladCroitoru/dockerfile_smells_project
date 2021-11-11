FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python python-dev python-setuptools python-pip \
    python-numpy python-scipy python-pymongo python-networkx python-yaml \
    python-psycopg2 python-matplotlib python-shapely python-pandas supervisor \
    mafft

RUN pip install cassandra-driver Flask redis rq requests==2.4.3 rollbar termcolor
