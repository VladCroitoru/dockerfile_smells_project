ARG REDIS_VER

FROM redis:${REDIS_VER}-alpine

ARG TARGETPLATFORM

ENV REDIS_VER="${REDIS_VER}"

RUN apk add --update --no-cache -t .wodby-redis-run-deps \
        bash \
        make \
        tzdata; \
    \
    apk add --update --no-cache -t .wodby-redis-build-deps \
        ca-certificates \
        tar \
        wget; \
    \
    dockerplatform=${TARGETPLATFORM:-linux/amd64};\
    gotpl_url="https://github.com/wodby/gotpl/releases/download/0.3.3/gotpl-${dockerplatform/\//-}.tar.gz"; \
    wget -qO- "${gotpl_url}" | tar xz --no-same-owner -C /usr/local/bin; \
    \
    apk del .wodby-redis-build-deps; \
    rm -rf /var/cache/apk/*

COPY templates /etc/gotpl/

COPY docker-entrypoint.sh /
COPY bin /usr/local/bin/

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD [ "redis-server" , "/etc/redis.conf" ]
