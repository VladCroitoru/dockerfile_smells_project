FROM ubuntu:14.04

MAINTAINER john.wang <wywincl@126.com>

#=========================================
# Install python and pip
#=========================================
RUN apt-get -y update \
    && apt-get install -y python python-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#=========================================
# Install robotframework and library.
#=========================================
RUN pip install robotframework
RUN pip install robotframework-selenium2library
RUN pip install requests
RUN pip install robotframework-requests

RUN mkdir /etc/robot
VOLUME /etc/robot
WORKDIR /etc/robot

#ADD entry-point.sh /entry-point.sh

#ENTRYPOINT ["/entry-point.sh"]
ENTRYPOINT ["robot"]

