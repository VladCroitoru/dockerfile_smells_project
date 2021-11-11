FROM alpine:latest

MAINTAINER Gamal Abdul Nasser <gamalanpro@gmail.com>

ENV JOB_SIZE 4096000
ENV BINLOG_SIZE 10485760

RUN apk add --no-cache beanstalkd

RUN mkdir -p /var/lib/beanstalkd
EXPOSE 11300
VOLUME [ "/var/lib/beanstalkd" ]

RUN export JOB_SIZE=${JOB_SIZE}
RUN export BINLOG_SIZE=${BINLOG_SIZE}

CMD beanstalkd -p 11300 -u beanstalk -z $JOB_SIZE -s $BINLOG_SIZE -b /var/lib/beanstalkd