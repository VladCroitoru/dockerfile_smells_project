# ------------------------------------------------------------------------------
# Start with a base image
# ------------------------------------------------------------------------------

FROM ubuntu:16.04
LABEL maintainer "Petr Cervenka <petr@cervenka.space>"
LABEL version="0.5"
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
# ------------------------------------------------------------------------------
# Provision the server
# ------------------------------------------------------------------------------

ENV DISPLAY :20.0
ENV SCREEN_GEOMETRY "2304x1440x24+32"
ENV CHROMEDRIVER_PORT 9515
ENV CHROMEDRIVER_WHITELISTED_IPS ""
ENV CHROMEDRIVER_URL_BASE ""

RUN mkdir /provision
ADD provision /provision
RUN /provision/provision.sh

ADD ./etc/supervisord.conf /etc/
ADD ./etc/supervisor /etc/supervisor
VOLUME [ "/var/log/supervisor" ]
# CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

EXPOSE 5900
EXPOSE 8081
