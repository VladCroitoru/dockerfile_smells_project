FROM mhart/alpine-node:6.2.1
MAINTAINER Gianluca Carucci <rucka@tiscalinet.it>

ENV STATSD_VERSION 0.8.0

ADD https://github.com/etsy/statsd/archive/v${STATSD_VERSION}.tar.gz /tmp/statsd.tar.gz
RUN mkdir -p /src && tar -xzvf /tmp/statsd.tar.gz -C /src && \
    rm /tmp/statsd.tar.gz
RUN mv /src/statsd-${STATSD_VERSION} /src/statsd

COPY config.js /etc/statsd/config.js

EXPOSE  8125/udp
CMD ["node", "/src/statsd/stats.js", "/etc/statsd/config.js"]
