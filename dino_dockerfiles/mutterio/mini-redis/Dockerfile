FROM  mutterio/mini-base

ENV REDIS_VERSION 3.0.2-r0

RUN apk-install redis=$REDIS_VERSION

ADD ./config/redis.conf /etc/redis.conf
ADD ./scripts/start.sh /start.sh

VOLUME ["/data"]

EXPOSE 6379

CMD ["/start.sh"]
