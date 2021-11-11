FROM phusion/baseimage:latest
MAINTAINER David Young <davidy@funkypenguin.co.nz>
#Based on the work of needo <needo@superhero.org>
#

# BUILD_DATE and VCS_REF are immaterial, since this is a 2-stage build, but our build
# hook won't work unless we specify the args
ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/htpc-cron.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################

# Set correct environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV HOME            /root
ENV LC_ALL          C.UTF-8
ENV LANG            en_US.UTF-8
ENV LANGUAGE        en_US.UTF-8

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Add a generic htpc user, which we'll reuse for all HTPC containers, and set UID predictable value (the meaning of 2 lives)
RUN useradd htpc -u 4242

ADD setupcron.sh /etc/my_init.d/setupcron.sh
RUN chmod +x /etc/service/*/run /etc/my_init.d/*

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################

VOLUME /config
