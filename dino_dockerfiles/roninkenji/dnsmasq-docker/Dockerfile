FROM roninkenji/slackware-base:latest
MAINTAINER roninkenji

RUN slackpkg -batch=on -default_answer=yes install dnsmasq

EXPOSE 53 67 69

ENTRYPOINT ["/usr/sbin/dnsmasq", "-k", "-C", "/etc/dnsmasq.d/dnsmasq.conf"]

