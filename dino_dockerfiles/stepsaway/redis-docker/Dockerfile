FROM redis:3.2-alpine
COPY redis.conf /usr/local/etc/redis/redis.conf
RUN mkdir -p /run/redis && chown -R redis:redis /run/redis
VOLUME ["/run/redis"]
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
