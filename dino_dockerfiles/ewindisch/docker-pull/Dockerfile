FROM ubuntu:14.04

# Install Docker
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9; \
    echo 'deb http://get.docker.io/ubuntu docker main' > /etc/apt/sources.list.d/docker.list; \
    apt-get update; \
    apt-get install -qqy lxc-docker-1.5.0

ADD docker-pull-save /usr/local/bin/

ENTRYPOINT ["docker-pull-save"]
