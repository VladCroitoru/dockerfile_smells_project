FROM alpine:latest
MAINTAINER support@tutum.co

ADD ntpd /etc/periodic/15min/ntpd
ADD run.sh /run.sh
CMD ["/run.sh"]
