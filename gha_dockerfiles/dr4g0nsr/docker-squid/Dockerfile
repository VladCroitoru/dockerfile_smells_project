FROM ubuntu:focal
LABEL maintainer="dragonmen@gmail.com"

ENV SQUID_CACHE_DIR=/var/spool/squid \
    SQUID_LOG_DIR=/var/log/squid \
    SQUID_USER=proxy \
    SQUID_VERSION=4.10

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y squid trickle nginx squid-cgi nano fcgiwrap
# && rm -rf /var/lib/apt/lists/*

COPY squid.conf /etc/squid/squid.conf
COPY squid-anonymous.conf /etc/squid/squid-anonymous.conf
COPY squid-delaypools.conf /etc/squid/squid-delaypools.conf
RUN rm /etc/nginx/sites-enabled/*
COPY cacheman.conf /etc/nginx/sites-available/cacheman.conf
RUN ln -s /etc/nginx/sites-available/cacheman.conf /etc/nginx/sites-enabled/cacheman.conf

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 3128/tcp
ENTRYPOINT ["/sbin/entrypoint.sh"]
