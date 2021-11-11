FROM existenz/webstack:7.3

COPY --chown=php:nginx . /www/public

RUN find /www/public -type d -exec chmod -R 755 {} \; \
    && find /www/public -type f -exec chmod -R 644 {} \; \
    && apk -U --no-cache add \
    php7-session \
    php7-json