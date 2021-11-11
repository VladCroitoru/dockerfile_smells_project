FROM debian:jessie
MAINTAINER Arnold Bechtoldt <mail@arnoldbechtoldt.com>

RUN export DEBIAN_FRONTEND=noninteractive; \
  apt-get update -qq && \
  apt-get upgrade -yV -o DPkg::Options::=--force-confold && \
  apt-get install -yV -o DPkg::Options::=--force-confold \
      wget && \
  wget --progress=dot:giga -O /usr/local/bin/etcdtool https://github.com/mickep76/etcdtool/releases/download/3.2/etcdtool-3.2-201602171504.linux.x86_64 && \
  chmod +x /usr/local/bin/etcdtool && \
  apt-get remove -yV wget && \
  apt-get autoremove -yV && \
  apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
