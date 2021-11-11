FROM codacy/base

LABEL maintainer="Rodrigo Fernandes <rodrigo@codacy.com>"

RUN \
  apt-get -y update && \
  apt-get -y install sudo && \
  apt-get -y install python && \
  apt-get -y install python-dev python-pip && \
  python -m pip install -I -U --upgrade pip && \
  \
  python -m pip install -I -U ansible==1.9.2 && \
  \
  apt-get -y remove --purge python-dev python-pip && \
  apt-get purge -y $(apt-cache search '~c' | awk '{ print $2 }') && \
  apt-get -y autoremove && \
  apt-get -y autoclean && \
  apt-get -y clean all && \
  rm -rf /root/.cache/pip && \
  rm -rf /root/.pip/cache && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/apt && \
  rm -rf /tmp/*
