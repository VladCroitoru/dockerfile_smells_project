FROM ubuntu:raring
MAINTAINER ewindisch@docker.com

RUN apt-get update
RUN apt-get install -qqy software-properties-common python-software-properties

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
RUN apt-add-repository 'deb http://get.docker.io/ubuntu docker main'
RUN apt-get update

RUN apt-get -qqy install socat lxc-docker

ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod 755 /usr/local/bin/wrapdocker
VOLUME /var/lib/docker
ENTRYPOINT wrapdocker
