FROM ubuntu:trusty
MAINTAINER juhani@juranki.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qqy update
RUN apt-get -qqy install curl htop wget
RUN curl -s https://get.docker.io/ubuntu/ | sh
RUN wget http://downloads.drone.io/latest/drone.deb
RUN dpkg -i drone.deb

EXPOSE 80
VOLUME ["/var/lib/docker", "/var/lib/drone"]
RUN echo 'DOCKER_OPTS="-H unix:///var/run/docker.sock"' >> /etc/default/docker

CMD /etc/init.d/docker start && /usr/local/bin/droned --port=:80 --datasource=/var/lib/drone/drone.sqlite

