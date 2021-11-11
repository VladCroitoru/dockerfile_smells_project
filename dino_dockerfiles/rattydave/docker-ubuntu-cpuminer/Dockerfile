#
# Dockerfile for cpuminer
# usage: docker run rattydave/docker-ubuntu-cpuminer --url xxxx --user xxxx --pass xxxx
# ex: docker run rattydave/docker-ubuntu-cpuminer --url stratum+tcp://ltc.pool.com:80 --user user1 --pass abcdef
#
#

FROM		ubuntu:16.04


RUN		apt-get update && \
      apt-get install -y  build-essential automake libcurl4-openssl-dev git make && \
      git clone https://github.com/pooler/cpuminer && \
      cd cpuminer && \
      ./autogen.sh && \
      ./configure CFLAGS="-O3"  && \
      make && \      
      apt-get -y autoclean && apt-get -y autoremove && \
      apt-get -y purge $(dpkg --get-selections | grep deinstall | sed s/deinstall//g) && \
      rm -rf /var/lib/apt/lists/*

WORKDIR		/cpuminer
ENTRYPOINT	["./minerd"]
