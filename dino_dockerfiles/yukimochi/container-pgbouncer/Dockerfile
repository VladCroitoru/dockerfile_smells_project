FROM alpine:latest AS builder

ARG PGBOUNCER_VERSION
RUN apk add -U --no-cache build-base libevent-dev c-ares-dev libressl-dev
RUN wget http://pgbouncer.github.io/downloads/files/$PGBOUNCER_VERSION/pgbouncer-$PGBOUNCER_VERSION.tar.gz && \
    wget http://pgbouncer.github.io/downloads/files/$PGBOUNCER_VERSION/pgbouncer-$PGBOUNCER_VERSION.tar.gz.sha256 -O - | sha256sum -c - && \
    tar -xf pgbouncer-$PGBOUNCER_VERSION.tar.gz && \
    rm pgbouncer-$PGBOUNCER_VERSION.tar.gz
WORKDIR pgbouncer-$PGBOUNCER_VERSION
RUN ./configure --prefix=/usr/local --with-libevent=libevent-prefix && \
    make && make install
WORKDIR /tmp/rootfs
RUN mkdir -p usr/bin usr/lib lib && \
    cp /usr/local/bin/pgbouncer usr/bin && \
    for lib in $(ldd usr/bin/pgbouncer | awk '{ print $(NF-1) }'); do \
    cp $lib .$lib; \
    done

FROM busybox

COPY --from=builder /tmp/rootfs /
RUN addgroup -S pgbouncer && \
    adduser -D -S pgbouncer -G pgbouncer && \
    mkdir -p /etc/pgbouncer /var/log/pgbouncer /var/run/pgbouncer && \
    chown pgbouncer /etc/pgbouncer /var/log/pgbouncer /var/run/pgbouncer
USER pgbouncer
VOLUME /etc/pgbouncer
EXPOSE 6432
CMD ["/usr/bin/pgbouncer", "/etc/pgbouncer/pgbouncer.ini"]
