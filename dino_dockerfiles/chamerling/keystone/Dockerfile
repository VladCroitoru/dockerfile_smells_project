# chamerling/keystone
#
# VERSION               1.0

FROM ubuntu:latest
MAINTAINER Christophe Hamerling "christophe.hamerling@gmail.com"

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update

RUN apt-get install -y keystone
RUN apt-get install -y sqlite

# Expose public and admin ports
EXPOSE 5000 35357

ADD scripts/run.sh run.sh

CMD /run.sh