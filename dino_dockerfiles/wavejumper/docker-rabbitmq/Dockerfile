FROM phusion/baseimage:0.9.6

ENV DEBIAN_FRONTEND noninteractive
 
RUN echo -e "#!/bin/sh \n\n exit 101" > /usr/sbin/policy-rc.d
RUN chmod +x /usr/sbin/policy-rc.d

RUN apt-get install -y wget
RUN wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc -O /tmp/rabbitmq.asc
RUN apt-key add /tmp/rabbitmq.asc
RUN rm /tmp/rabbitmq.asc
 
RUN echo "deb http://www.rabbitmq.com/debian/ testing main" > /etc/apt/sources.list.d/rabbitmq.list
RUN apt-get update
RUN apt-get install -y rabbitmq-server
 
RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_management
 
EXPOSE 5672 15672 4369
 
CMD /usr/sbin/rabbitmq-server
