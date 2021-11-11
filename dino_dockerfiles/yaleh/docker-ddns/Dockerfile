# shadowsocks
#
# VERSION 0.0.1

FROM ubuntu:14.04
MAINTAINER Yale Huang <yale.huang@trantect.com>

RUN apt-get update && \
    apt-get install -y inadyn
RUN mkdir -p /etc/inadyn
VOLUME ["/etc/inadyn"]
CMD ["/usr/bin/inadyn", "-F", "/etc/inadyn/inadyn.conf"]

