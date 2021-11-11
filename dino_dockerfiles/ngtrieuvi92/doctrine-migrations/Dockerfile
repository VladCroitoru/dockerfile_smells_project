# Build from alipine
FROM alpine:3.4
MAINTAINER vi.nt <vi.nt@geekup.vn>

# Install doctrine-migation
RUN apk --update add curl php5 php5-mysql php5-json php5-zlib php5-phar php5-pdo_mysql && \
    curl -sS -0L https://github.com/doctrine/migrations/releases/download/1.4.1/doctrine-migrations.phar -o /usr/bin/doctrine-migrations && \
    chmod +x /usr/bin/doctrine-migrations && \
    apk del curl && \
    rm -rf /var/cache/apk/*

# Create /data directory and set it as volume then set work dir to /data
RUN mkdir /data
VOLUME ["/data"]
WORKDIR /data

ENTRYPOINT ["doctrine-migrations"]
