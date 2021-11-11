FROM python:2.7
MAINTAINER Eloy Coto <eloy.coto@gmail.com>

ADD  req.txt /
RUN pip install -r /req.txt

ADD run.py /

VOLUME /opt/junos_statsd/
ENTRYPOINT /run.py
