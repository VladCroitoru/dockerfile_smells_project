FROM fedora:23

MAINTAINER Erik Osterman "erik@cloudposse.com"

RUN dnf -y --setopt=tsflags=nodocs install ftp://195.220.108.108/linux/mageia/distrib/cauldron/x86_64/media/core/release/logrotate-3.9.2-1.mga6.x86_64.rpm && \
    dnf clean all

ENV LOGROTATE_PATHS   /var/log/*.log
ENV LOGROTATE_OPTIONS rotate 72, dateext, dateformat -%Y%m%d_%H%M%S, compress, missingok, notifempty, nocreate, su root root
ENV LOGROTATE_CONFIG  /etc/logrotate.conf
ENV LOGROTATE_STATE   /var/lib/logrotate.state

ADD start /start

USER root

ENTRYPOINT ["/start"]
CMD -f -s $LOGROTATE_STATE $LOGROTATE_CONFIG


