FROM php:8.1.0RC5-fpm-alpine

ARG BUILD_DATE
ARG BUILD_VERSION
ARG VCS_URL
ARG VCS_REF
ARG VCS_BRANCH
# See http://label-schema.org/rc1/ and https://microbadger.com/labels
LABEL maintainer="Thomas Appel <thomas.appel@tmt.de>" \
    org.label-schema.name="PHP 8.1 - FastCGI Process Manager" \
    org.label-schema.description="PHP-FPM 8.1 (with some more extensions installed)" \
    org.label-schema.vendor="TMT GmbH & Co. KG" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.build-date="${BUILD_DATE:-unknown}" \
    org.label-schema.version="${BUILD_VERSION:-unknown}" \
    org.label-schema.vcs-url="${VCS_URL:-unknown}" \
    org.label-schema.vcs-ref="${VCS_REF:-unknown}" \
    org.label-schema.vcs-branch="${VCS_BRANCH:-unknown}"

ENV EXT_DEPS \
  pkgconfig \
  libxml2-dev \
  libxslt \
  libxslt-dev \
  gnupg \
  dialog \
  zlib-dev \
  libzip-dev \
  icu-dev \
  gettext-dev
ENV COMPOSER_ALLOW_SUPERUSER 1

# hadolint ignore=SC2086,DL3017,DL3018,DL4006
RUN set -xe; \
  apk --no-cache update && apk --no-cache upgrade \
  && apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/community gnu-libiconv \
  && apk add --no-cache $EXT_DEPS \
  && apk add --no-cache --virtual .build-deps $PHPIZE_DEPS \
  && docker-php-ext-configure xsl \
  && docker-php-ext-install xsl \
  && docker-php-ext-enable xsl \
  && docker-php-ext-configure intl \
  && docker-php-ext-install intl \
  && docker-php-ext-configure gettext \
  && docker-php-ext-install gettext \
  && docker-php-ext-configure zip \
  && docker-php-ext-install zip \
  && docker-php-ext-configure opcache \
  && docker-php-ext-install opcache \
  && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
  && chmod +x /usr/local/bin/composer \
  # Cleanup build deps
  #  8 # clean up build deps
  && apk del .build-deps \
  && rm -rf /tmp/* /var/cache/apk/*

  ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php
