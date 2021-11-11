FROM  mhart/alpine-node:0.10.41
MAINTAINER Marcello_deSales@intuit.com

RUN \
  apk --update add python make gcc g++ && \
  rm -rf /var/cache/apk/* && \
  USER=root npm install --global statsd && \
  apk --purge del python make gcc g++

WORKDIR /usr/lib/node_modules/statsd/

ADD ./config.js /usr/lib/node_modules/statsd/config.js
ADD ./backends/wavefront.js /usr/lib/node_modules/statsd/backends/wavefront.js

EXPOSE \
  # StatsD UDP
  8125/udp \
  # StatsD Admin
  8126

CMD ["/usr/bin/node", "stats.js", "config.js"]
