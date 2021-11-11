FROM redis:4.0.9-alpine

ENV SENTINEL_QUORUM 1
ENV SENTINEL_DOWN_AFTER 1000
ENV SENTINEL_FAILOVER 1000
ENV REDIS_MASTER redis-master

RUN mkdir -p /redis

WORKDIR /redis

COPY ./sentinel/sentinel.conf .
COPY ./sentinel/sentinel-entrypoint.sh /usr/local/bin/sentinel-entrypoint.sh

RUN chown redis:redis /redis/* && \
    chmod +x /usr/local/bin/sentinel-entrypoint.sh

EXPOSE 26379

ENTRYPOINT ["sentinel-entrypoint.sh"]

