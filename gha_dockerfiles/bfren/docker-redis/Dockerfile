FROM bfren/alpine-s6:alpine3.14-2.2.20

EXPOSE 6379

ENV \
    # change this to 'yes' if you are exposing Redis to the internet,
    # and set REDIS_BIND to the server IP (you should not normally do this!)
    REDIS_PROTECTED_MODE=no \
    # leave this blank to bind Redis to all network interfaces - only do
    # this if you are using Redis within a private Docker network
    REDIS_BIND= \
    # log level: debug, verbose, notice, warning
    REDIS_LOG_LEVEL=notice \
    # the maximum number of clients this instance can serve
    REDIS_MAX_CLIENTS=10000 \
    # see https://redis.io/topics/persistence
    REDIS_APPEND_ONLY=no \
    # see http://antirez.com/post/redis-persistence-demystified.html
    REDIS_APPEND_FSYNC=everysec

COPY ./overlay /
COPY ./REDIS_BUILD /tmp/VERSION

RUN bf-install

VOLUME [ "/data" ]
