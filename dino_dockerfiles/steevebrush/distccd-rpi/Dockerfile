FROM phusion/baseimage:latest
MAINTAINER Stéphane BROSSE "steevebrush@gmail.com"
LABEL description="distcc pi arm cross bash -compiler node"

CMD ["/sbin/my_init"]

RUN mkdir /etc/service/distccd && \
    apt-get update && apt-get install -y \
    distcc

ADD distccd.sh /etc/service/distccd/run 

EXPOSE 3632

VOLUME ["/tools"]

RUN chmod +x /etc/service/distccd/run && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENV PATH="/tools/bin:${PATH}"
