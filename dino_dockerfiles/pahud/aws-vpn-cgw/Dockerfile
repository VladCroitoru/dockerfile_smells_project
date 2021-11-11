#FROM resin/rpi-raspbian:jessie
FROM ubuntu:trusty

MAINTAINER Pahud Hsieh <pahudnet@gmail.com>

ENV \
  DEBIAN_FRONTEND=noninteractive \
  TERM=xterm-color


RUN apt-get update && apt-get -y install --no-install-recommends \
  iputils-ping net-tools iptables openswan ipsec-tools lsof iptables wget supervisor 

WORKDIR /root

ADD startup.sh /
ADD ./etc/ipsec.conf /etc/
ADD ./etc/ipsec.d/home-to-aws.conf /etc/ipsec.d/


EXPOSE 500 4500

CMD ["/startup.sh"]
#CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf",  "--nodaemon"]
