FROM maskwang/docker-nginx-php:latest

MAINTAINER Mask Wang, mask.wang.cn@gmail.com

ENV HOME /root

RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

CMD ["/sbin/my_init"]

# Nginx-Python Installation
RUN apt-get update
RUN apt-get install -y g++ libmysqlclient-dev python-dev python-pip\
               libzmq-dev pkg-config libtool autoconf

RUN pip install MySQL-python croniter pyzmq

EXPOSE 80
# End Nginx-Python

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
