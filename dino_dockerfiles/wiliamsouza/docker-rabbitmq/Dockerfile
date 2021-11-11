# RabbitMQ server generic image source
#
# Version 0.1.0

FROM ubuntu:12.04

MAINTAINER Wiliam Souza <wiliamsouza83@gmail.com>

# base
ENV LANG en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN locale-gen en_US en_US.UTF-8
RUN dpkg-reconfigure locales
RUN apt-get update

RUN apt-get install -y python-software-properties

# supervisor
RUN apt-get install supervisor -y
RUN update-rc.d -f supervisor disable

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# start script
ADD startup /usr/local/bin/startup
RUN chmod +x /usr/local/bin/startup

CMD ["/usr/local/bin/startup"]

# environment

# sources

# ppas

# rabbitmq-server 
RUN apt-get install rabbitmq-server -y
RUN update-rc.d -f rabbitmq-server disable

VOLUME ["/var/log/rabbitmq", "/var/lib/rabbitmq"]

EXPOSE 5672
