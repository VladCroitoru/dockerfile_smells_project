FROM golang:1.7-alpine

RUN apk update && \
    apk upgrade && \
    apk add --no-cache git && \
    rm  -rf /tmp/* /var/cache/apk/* && \
    go get github.com/oxalide/phpfpm-prometheus-exporter

ENV LISTEN_KEY "localhost:9000"
ENV STATUS_KEY "/status"
ENV POOL_NAME "www"
ENV METRICS_ADDR ":9101"

ADD run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 9101 
ENTRYPOINT ["/run.sh"]
