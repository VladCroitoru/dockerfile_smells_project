FROM gliderlabs/alpine:3.2

ENV USER root
RUN apk --update add python nodejs bash

EXPOSE 8125/udp
EXPOSE 8125

# RUN npm install -g statsd statsd-librato-backend@0.1.7 #used for legacy source metrics
RUN npm install -g statsd statsd-librato-backend
RUN mkdir -p /etc/statsd
ADD ./config.js /etc/statsd/

#temporary fix until https://github.com/librato/statsd-librato-backend/pull/81 gets accepted
ADD ./librato.js /usr/lib/node_modules/statsd-librato-backend/lib/

ENTRYPOINT ["statsd", "/etc/statsd/config.js"]
