FROM ubuntu

MAINTAINER Denis Golovachev <borov.htid@gmail.com>

## DEPENDENCIES ##
## add mesosphere repo and keys
RUN echo "deb http://repos.mesosphere.io/$(lsb_release -is | tr '[:upper:]' '[:lower:]') $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/mesosphere.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF

RUN apt-get update
RUN apt-get install --assume-yes supervisor mesos deimos python-pip python-dev python-protobuf docker.io mesos python-software-properties curl default-jdk

RUN ln -sf /usr/bin/docker.io /usr/local/bin/docker
RUN mkdir -p /etc/mesos-master

ADD http://downloads.mesosphere.io/marathon/marathon-0.6.1/marathon-0.6.1.tgz /marathon.tgz
RUN tar xzf marathon.tgz

#Define volumes
VOLUME ["/etc/supervisor/conf.d/"]
CMD ["/usr/bin/supervisord"]
