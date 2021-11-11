FROM alpine:latest

RUN apk -U add python

COPY mesos-statsd.py /bin
COPY mesos-statsd.sh /bin

ENTRYPOINT ["mesos-statsd.sh"]
