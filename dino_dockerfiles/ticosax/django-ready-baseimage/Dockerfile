FROM phusion/baseimage:latest

MAINTAINER Nicolas Delaby "nicolas@ezeep.com"

RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

RUN apt-get update &&\
    apt-get install -qq build-essential\
                        python-pip python-dev\
                        libpq-dev\
                        libmemcached-dev\
                        git-core\
                        libxml2-dev\
                        libxslt-dev\
                        &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install -U pip wheel setuptools
