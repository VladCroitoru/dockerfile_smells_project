FROM alpine:latest
RUN apk add --update netcat-openbsd && rm -rf /var/cache/apk/*
COPY waiter.sh /
ENTRYPOINT ["/waiter.sh"]
