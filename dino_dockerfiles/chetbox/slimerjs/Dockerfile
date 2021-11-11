# dockerhub - A repository for various dockerfiles
# For more information; http://github.com/cmfatih/dockerhub
#
# slimerjs
#
# Usage
#   docker run chetbox/slimerjs /usr/bin/slimerjs -v
#   docker run chetbox/slimerjs /usr/bin/casperjs | head -n 1
#   docker run -v `pwd`:/mnt/test chetbox/slimerjs /usr/bin/slimerjs /mnt/test/test.js

FROM ubuntu:14.04

MAINTAINER chetbox

# Env
ENV SLIMERJS_VERSION_TYPE nightlies
ENV SLIMERJS_VERSION_F 0.10.0pre

# Commands
RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y vim git wget xvfb libxrender-dev libasound2 libdbus-glib-1-2 libgtk2.0-0 bzip2 && \
  mkdir -p /srv/var && \
  wget -qO /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-x86_64.tar.bz2 http://download.slimerjs.org/$SLIMERJS_VERSION_TYPE/$SLIMERJS_VERSION_F/slimerjs-$SLIMERJS_VERSION_F-linux-x86_64.tar.bz2 && \
  tar -xjf /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-x86_64.tar.bz2 -C /tmp && \
  rm -f /tmp/slimerjs-$SLIMERJS_VERSION_F-linux-x86_64.tar.bz2 && \
  mv /tmp/slimerjs-$SLIMERJS_VERSION_F/ /srv/var/slimerjs && \
  echo '#!/bin/bash\nxvfb-run -a /srv/var/slimerjs/slimerjs "$@"' > /srv/var/slimerjs/slimerjs.sh && \
  chmod 755 /srv/var/slimerjs/slimerjs.sh && \
  ln -s /srv/var/slimerjs/slimerjs.sh /usr/bin/slimerjs && \
  git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs && \
  echo '#!/bin/bash\n/srv/var/casperjs/bin/casperjs --engine=slimerjs "$@"' >> /srv/var/casperjs/casperjs.sh && \
  chmod 755 /srv/var/casperjs/casperjs.sh && \
  ln -s /srv/var/casperjs/casperjs.sh /usr/bin/casperjs && \
  apt-get autoremove -y && \
  apt-get clean all

# Default command
CMD ["/usr/bin/slimerjs"]
