FROM alpine:3.2

RUN apk --update add redis && \
    sed -i 's/^\(bind .*\)$/# \1/' /etc/redis.conf && \
    sed -i 's/^\(daemonize .*\)$/# \1/' /etc/redis.conf && \
    sed -i 's/^\(logfile .*\)$/# \1/' /etc/redis.conf

EXPOSE 6379

ENTRYPOINT ["redis-server", "/etc/redis.conf"]