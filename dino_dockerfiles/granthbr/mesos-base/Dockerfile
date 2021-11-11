FROM ubuntu:14.04

MAINTAINER Brandon Grantham <brandon.grantham@gmail.com>
#updated from mesoscloud repo 
#changes: RUN Command has been optimized and base pushed online


RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
echo deb http://repos.mesosphere.io/ubuntu trusty main > /etc/apt/sources.list.d/mesosphere.list && \
apt-get update && \
apt-get -y install mesos=0.24.1-0.2.35.ubuntu1404 && curl -fLsS https://get.docker.com/ | sh

ENV MESOS_WORK_DIR /tmp/mesos

VOLUME /tmp/mesos

COPY entrypoint.sh /

ENTRYPOINT ["./entrypoint.sh"]
