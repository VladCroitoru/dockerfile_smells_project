FROM alpine:3.4

RUN apk add -U redis && rm -rf /var/cache/apk/*

COPY redis-master.conf /etc/config/redis-master.conf
COPY redis-slave.conf /etc/config/redis-slave.conf
COPY redis-sentinel.conf /etc/config/redis-sentinel.conf

CMD [ "bash", "-c", ""trap : TERM INT; sleep infinity & wait"" ]

ENTRYPOINT []
