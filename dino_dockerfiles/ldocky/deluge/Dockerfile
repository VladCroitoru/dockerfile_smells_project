FROM ubuntu:focal
MAINTAINER ldocky 

VOLUME ["/config", "/complete", "/incomplete", "/blackhole", "/m"]

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN	apt-get install -y software-properties-common 
RUN	add-apt-repository -y ppa:deluge-team/stable
RUN	apt-get update
RUN apt-get install -y deluged deluge-web

EXPOSE 8112 58846

RUN apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY /startup.sh /startup.sh
RUN chmod 777 /startup.sh

ENTRYPOINT ["/startup.sh"]
