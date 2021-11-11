####
#
# Squid3 proxy with or without auth
#
# https://github.com/reddec/squid
#
###
FROM ubuntu:14.04
MAINTAINER RedDec
RUN apt-get update && apt-get upgrade -y && apt-get install -y squid3
RUN mkdir -p /etc/squid3/conf.d/enabled
RUN mkdir -p /etc/squid3/conf.d/disabled
RUN mkdir -p /etc/squid3/conf.d/extra
RUN mkdir -p /passwords
ADD squid.conf /etc/squid3/squid.conf
ADD auth.conf /etc/squid3/conf.d/enabled/auth.conf
ADD noauth.conf /etc/squid3/conf.d/disabled/noauth.conf
ADD utils/with_auth.sh /usr/local/bin/auth
ADD utils/without_auth.sh /usr/local/bin/noauth
ADD keys /passwords/keys
EXPOSE 3128
VOLUME /passwords
