FROM alpine:edge
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN apk --no-cache --progress add pgbouncer

COPY pgbouncer.ini /etc/pgbouncer/pgbouncer.ini
COPY entrypoint.sh /

ENV DB=database HOST=host PORT=5432 \
    CLIENT_IDLE_TIMEOUT=0.0 IGNORE_STARTUP_PARAMETERS="extra_float_digits" \
    DEFAULT_POOL_SIZE=90 MAX_CLIENT_CONN=500 SERVER_RESET_QUERY="DISCARD ALL" \
    POOL_MODE=transaction LISTEN_PORT=6432

EXPOSE $LISTEN_PORT

ENTRYPOINT ["/entrypoint.sh"]
CMD ["-u", "pgbouncer", "/etc/pgbouncer/pgbouncer.ini"]