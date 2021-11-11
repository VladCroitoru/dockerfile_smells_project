FROM ubuntu:16.04
MAINTAINER Pasi Lammi <pasi@pashi.net>

# update latest security updates 2018-01-19

RUN apt-get update && apt-get -y install python-pip python-dev libssl-dev libffi-dev
RUN pip install --upgrade pip
RUN pip install --pre azure && pip install msrest && pip install msrestazure
RUN mkdir -p /data /app
WORKDIR /app
EXPOSE 8000
VOLUME ["/data"]
