# Created on Jul. 1, 2016
# @author: Sam

FROM ubuntu:16.04

MAINTAINER samsam2310@gmail.com

# install python2.7 && python-dev && wget && cron/crontab && gcc
RUN apt-get update && apt-get install -y python2.7 python-dev wget cron build-essential
# install pip
RUN wget https://bootstrap.pypa.io/get-pip.py -O- | python
# install python-lxml
RUN apt-get update && apt-get install -y python-lxml
