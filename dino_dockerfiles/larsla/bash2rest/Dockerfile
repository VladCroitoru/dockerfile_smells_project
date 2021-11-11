# Bash2REST
# Execute bash scripts via a REST interface
#

FROM ubuntu:14.04

MAINTAINER Lars Larsson "lars.la@gmail.com"

RUN apt-get update && apt-get install -y python-pip jq && apt-get clean

ADD . /bash2rest
RUN pip install -r /bash2rest/requirements.txt

ADD scripts /scripts

VOLUME /logs

CMD /usr/bin/python /bash2rest/bash2rest.py
