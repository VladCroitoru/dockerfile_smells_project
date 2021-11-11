FROM debian:wheezy

MAINTAINER Victor Klos "victor@victorklos.nl"

ADD apt/jessie.list /etc/apt/sources.list.d/jessie.list
ADD apt/jessie /etc/apt/preferences.d/jessie
RUN apt-get update
RUN apt-get install -y dpkg-dev
RUN apt-get build-dep -y opensmtpd

VOLUME /srv/deb
WORKDIR /srv/deb
ENTRYPOINT [ "/usr/bin/apt-get", "source", "opensmtpd", "--compile" ]
