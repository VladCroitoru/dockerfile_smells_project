FROM python:3.5-slim

MAINTAINER Sahand Hariri sahandha@gmail.com
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*
RUN apt-get -qq update
RUN apt-get -qq -y install wget curl
RUN sudo apt-get -qq -y install software-properties-common apt-utils

RUN sudo apt-get install -y python-pip python-dev build-essential
RUN sudo apt-get install -y git
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install  matplotlib
RUN pip install seaborn
RUN apt-get install -y python-tk

RUN apt-get install -y default-jre; exit 0

RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2-bin-hadoop2.7.tgz
RUN tar xvf spark-2.0.2-bin-hadoop2.7.tgz
RUN rm spark-2.0.2-bin-hadoop2.7.tgz
RUN mv spark-2.0.2-bin-hadoop2.7 /opt/spark
RUN pip install findspark
RUN pip install tornado
RUN pip install motor

RUN git clone https://github.com/sahandha/iso_forest.git /root/iso_forest
RUN pip install /root/iso_forest

#RUN apt-get install -y gzip tar
#RUN tar -zcvf iso_forest.tar.gzip /root/iso_forest



EXPOSE 8888

Add iso_server /external/server
Add iso_forest-master.zip /external

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV SPARK_HOME=/opt/spark
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:$PYTHONPATH
ENV ISOFOREST=/external/server

RUN apt-get install -y vim; exit 0
