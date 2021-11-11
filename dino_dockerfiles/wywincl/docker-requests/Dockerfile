FROM python:2.7.12

MAINTAINER john.wang <wywincl@126.com>

#=========================================
# Install requests and bs4 library.
#=========================================

RUN pip install -U requests
RUN pip install -U beautifulsoup4

#============
# workspace
#============
RUN mkdir /etc/robot
VOLUME /etc/robot
WORKDIR /etc/robot
