FROM alpine:3.5

RUN apk update && \
    apk upgrade && \
    apk add collectd collectd-ping collectd-network

COPY collectd.conf /etc/collectd/

CMD exec collectd -f
