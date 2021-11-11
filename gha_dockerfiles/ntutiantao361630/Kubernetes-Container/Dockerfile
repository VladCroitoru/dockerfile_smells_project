FROM ubuntu:latest
MAINTAINER taochungying@gmail.com

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install bs4
COPY app.py .
