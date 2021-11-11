FROM nodesource/trusty
MAINTAINER Nikolay Popov <dev@nicolnx.com>

RUN apt-get update && apt-get install -y wget python-pip locales libjson-perl && localedef en_US.UTF-8 -i en_US -f UTF-8 && pip install awscli
RUN wget -P /tmp --no-check-certificate https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/14.04/x86_64/chefdk_0.11.2-1_amd64.deb
RUN dpkg -i /tmp/chefdk_0.11.2-1_amd64.deb
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs
