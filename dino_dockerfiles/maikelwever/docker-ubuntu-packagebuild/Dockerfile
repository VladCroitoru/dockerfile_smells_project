FROM ubuntu:trusty
MAINTAINER Maikel Wever <maikelwever@gmail.com>

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y build-essential git sudo fakeroot python debianutils debhelper devscripts

ADD sudoers /etc/sudoers
RUN chmod 0400 /etc/sudoers
