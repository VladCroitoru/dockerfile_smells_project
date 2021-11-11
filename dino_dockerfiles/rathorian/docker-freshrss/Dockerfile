FROM alpine:3.12

ARG FRESHRSS_VER=1.17.0

ENV UID=991 GID=991 \
    UPLOAD_MAX_SIZE=10M \
    MEMORY_LIMIT=128M \
    CRON_PERIOD=15m \
    TZ=Europe/Paris

RUN apk add --no-progress --no-cache \
    tar \
    tzdata \
    ca-certificates \
    nginx \
    php7 \
    php7-fpm \
    php7-ctype \
    php7-curl \
    php7-dom \
    php7-fileinfo \
    php7-gmp \
    php7-iconv \
    php7-intl \
    php7-json \
    php7-mbstring \
    php7-mysqli \
    php7-pdo \
    php7-pdo_mysql \
    php7-pdo_pgsql \
    php7-pdo_sqlite \
    php7-pgsql \
    php7-session \
    php7-simplexml \
    php7-sqlite3 \
    php7-xml \
    php7-xmlreader \
    php7-zip \
    php7-zlib \
    sqlite \
    su-exec \
    s6 \
 && mkdir freshrss && cd freshrss \
 && wget -qO- https://github.com/FreshRSS/FreshRSS/archive/${FRESHRSS_VER}.tar.gz | tar xz --strip 1 \
 && mv data data_tmp \
 && apk del tar \
 && rm -rf /var/cache/apk/*

COPY rootfs /

RUN chmod +x /usr/local/bin/run.sh /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*

VOLUME /freshrss/data

EXPOSE 8888

LABEL description="A free, self-hostable aggregator" \
      version="FreshRSS v${FRESHRSS_VER}" \
      maintainer="rathorian@gmail.com"

CMD ["run.sh"]
