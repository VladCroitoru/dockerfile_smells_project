FROM redis:3-alpine

MAINTAINER Cross Zheng (zhengxin@twitter.com)

ENV REQUIREPASS 123456
ENV SENTINEL_QUORUM 2
ENV CLIENTPORT 26379
ENV MASTERHOST localhost
ENV MASTERPORT 6479
ENV MASTERNAME mymaster

## sentinel default values, will not appear in the sentinel.conf, but can be replaced from docker-compose
ENV SENTINEL_DOWN_AFTER 30000
ENV SENTINEL_FAILOVER 180000


## sentinel.conf: $CLIENTPORT also assigned here
ADD sentinel.conf /etc/redis/sentinel.conf
RUN chown redis:redis /etc/redis/sentinel.conf

EXPOSE $CLIENTPORT

COPY sentinel-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["sentinel-entrypoint.sh"]
