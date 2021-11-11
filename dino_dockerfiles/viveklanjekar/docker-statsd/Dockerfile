FROM    node:7-alpine
MAINTAINER Janusz Korczak <januszkorczak128@gmail.com>

WORKDIR /opt

RUN apk add --update ca-certificates wget && \
    update-ca-certificates && \
    wget https://github.com/etsy/statsd/archive/master.zip && \
    unzip master.zip && \
    rm -f master.zip && \
    mv /opt/statsd-master /opt/statsd && \
    npm install -g generic-pool && \
    mkdir /etc/statsd

ADD config.js /etc/statsd/config.js
ADD backends/smart_repeater.js /opt/statsd/backends/smart_repeater.js

ENV NODE_PATH /usr/local/lib/node_modules

EXPOSE 8125/udp

CMD [ "/usr/local/bin/node", "/opt/statsd/stats.js", "/etc/statsd/config.js" ]
