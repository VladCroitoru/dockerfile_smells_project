FROM ubuntu:14.04
MAINTAINER mrbar42@gmail.com

ENV VERSION=0.27.2-2.0.15.ubuntu1404
# list available versions - apt-cache show mesos | grep Version
#Version: 0.27.1-2.0.226.ubuntu1404
#Version: 0.27.0-0.2.190.ubuntu1404
#Version: 0.26.0-0.2.145.ubuntu1404
#Version: 0.25.0-0.2.70.ubuntu1404
#Version: 0.24.1-0.2.35.ubuntu1404

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \
echo deb http://repos.mesosphere.io/ubuntu trusty main > /etc/apt/sources.list.d/mesosphere.list && \
apt-get update && \
apt-get -y install mesos=${VERSION} docker.io

ENV MESOS_WORK_DIR /tmp/mesos
VOLUME /tmp/mesos

# for master - ENTRYPOINT ["mesos-master"]
# for slave - ENTRYPOINT ["mesos-slave"]