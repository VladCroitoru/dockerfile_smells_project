FROM ubuntu
MAINTAINER Ron Arts <ron.arts@gmail.com>

RUN apt-get update && \
 apt-get install -y \
 bmon \
 curl \ 
 dnsutils \
 iftop \
 iperf \
 iputils-ping \
 lynx \
 mtr-tiny \
 net-tools \
 netcat \
 nmap \
 openssh-client \
 strace \
 sysstat \
 tcpdump \
 tcptraceroute \
 traceroute \
 telnet \
 vim \ 
 wget \ 
 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . /root/scripts

CMD [ "/bin/bash" ]
