FROM phusion/baseimage

ENV SET_PASS false

RUN echo '#!/bin/sh' "\nexit 0" >  /usr/sbin/policy-rc.d

RUN apt-get update -qq && apt-get install -y software-properties-common python-software-properties && apt-get upgrade -y -qq
RUN apt-add-repository -y ppa:chris-lea/redis-server
RUN apt-get update -qq && apt-get install -y redis-server=2:2.8.*

#prevent daemonization and bind to 0.0.0.0
RUN sed -i 's/daemonize yes/daemonize no/g' /etc/redis/redis.conf
RUN sed -i 's/bind 127.0.0.1/bind 0.0.0.0/g' /etc/redis/redis.conf

RUN mkdir /etc/service/redis
ADD run.sh /etc/service/redis/run
RUN chmod 755 /etc/service/redis/run

EXPOSE 6379
VOLUME ["/var/lib/redis"]

CMD ["/sbin/my_init"]