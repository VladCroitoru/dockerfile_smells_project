FROM ubuntu:trusty
MAINTAINER Maikel Wever <maikelwever@gmail.com>

RUN sed -i 's/archive/nl.archive/g' /etc/apt/sources.list  
RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y firefox xvfb python3 python3-pip python3-dev libpq-dev git subversion mercurial python-virtualenv libffi-dev openjdk-7-jre nodejs-legacy npm

RUN useradd -ms /bin/bash ciuser
RUN groupadd wheel
RUN usermod -a -G wheel ciuser

ADD sudoers /etc/sudoers
ADD xvfb /etc/init.d/xvfb
RUN chmod 0400 /etc/sudoers
RUN chmod 0700 /etc/init.d/xvfb

USER ciuser
