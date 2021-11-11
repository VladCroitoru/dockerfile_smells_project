FROM phusion/baseimage

ENV DEBIAN_FRONTEND noninteractive
RUN echo '#!/bin/sh' "\nexit 0" >  /usr/sbin/policy-rc.d

RUN apt-get update && apt-get install -y wget
RUN wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
RUN apt-key add rabbitmq-signing-key-public.asc
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list
RUN apt-get update
RUN apt-get -y -q install rabbitmq-server
RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_management

EXPOSE 5672 55672 15672

RUN mkdir /etc/service/rabbitmq
ADD run.sh /etc/service/rabbitmq/run
RUN chmod 755 /etc/service/rabbitmq/run

CMD ["/sbin/my_init"]