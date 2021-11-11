FROM alpine

ENV GATEWAY_PORT 19531
RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

ADD docker_entry.sh /docker_entry.sh

ENTRYPOINT ["/docker_entry.sh"]




