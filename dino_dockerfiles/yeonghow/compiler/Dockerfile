FROM php:fpm
MAINTAINER Tan Yeong How "yeonghowtan@gmail.com"

RUN apt-get update

# AppArmor
RUN apt-get install -y apparmor apparmor-profiles apparmor-utils auditd

# Python
RUN apt-get install -y libffi-dev libssl-dev python-dev python-pip pypy python-pypy.sandbox
RUN \
    ln -s /usr/lib/python2.7/dist-packages/pypy/ /usr/lib/pypy/dist-packages/ && \
    pypy --version && \
    ln -s /usr/lib/pypy-sandbox/x86_64-linux-gnu/pypy-c-sandbox /usr/lib/pypy-sandbox/pypy-c-sandbox

# PHP
RUN apt-get install -y php5-cli

# C
RUN apt-get install -y gcc

# Java
RUN apt-get install -y python-software-properties software-properties-common
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java8-installer


RUN chmod o-x /bin/*
RUN chmod o+x /bin/bash
RUN chmod o+x /bin/dash


USER www-data
