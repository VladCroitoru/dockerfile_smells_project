# docker build -t yuanying/node-exporter-smartmon .
# docker run --privileged yuanying/node-exporter-smartmon
FROM alpine:latest
MAINTAINER OTSUKA, Yuanying "yuan-docker@fraction.jp"

COPY smartmon.sh /

RUN apk --no-cache --update add smartmontools bash; \
    rm -rf /var/cache/apk/*; \
    chmod +x /smartmon.sh

ENTRYPOINT ["/smartmon.sh"]
