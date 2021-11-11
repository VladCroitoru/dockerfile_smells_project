FROM phusion/baseimage
ENV DEBIAN_FRONTEND=noninteractive

#add this for mustache templates in config files
ADD https://raw.githubusercontent.com/tests-always-included/mo/master/mo /usr/bin/
RUN chmod a+rx /usr/bin/mo

RUN apt-get update && \
    apt-get install -y gosu && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
