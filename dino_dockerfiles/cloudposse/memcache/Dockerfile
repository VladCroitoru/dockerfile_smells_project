# Latest Ubuntu LTS
FROM ubuntu:14.04

MAINTAINER  Erik Osterman "e@osterman.com"

# System 
ENV TIMEZONE Etc/UTC
ENV DEBIAN_FRONTEND noninteractive

ENV MEMCACHED_BIND 0.0.0.0
ENV MEMCACHED_MEM 64
ENV MEMCACHED_USER memcache
ENV MEMCACHED_PORT 11211

# Locale specific
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8


# Update the package repository
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y memcached && \
    apt-get install -y locales && \
    locale-gen $LANGUAGE && dpkg-reconfigure locales && \
    echo "$TIMEZONE" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD start /start
USER memcache
EXPOSE 11211
CMD /start -v -m $MEMCACHED_MEM -p $MEMCACHED_PORT -l $MEMCACHED_BIND -u $MEMCACHED_USER
