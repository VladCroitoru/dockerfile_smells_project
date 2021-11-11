FROM ghcr.io/unb-libraries/nginx-php:1.x-7.x
MAINTAINER Jacob Sanford <libsystems_at_unb.ca>

LABEL ca.unb.lib.generator="drupal8" \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.description="docker-drupal is the base drupal image at UNB Libraries." \
  org.label-schema.name="drupal" \
  org.label-schema.url="https://github.com/unb-libraries/docker-drupal" \
  org.label-schema.vcs-ref="8.x-3.x" \
  org.label-schema.vcs-url="https://github.com/unb-libraries/docker-drupal" \
  org.label-schema.version=$VERSION \
  org.opencontainers.image.source="https://github.com/unb-libraries/docker-drupal"

ENV COMPOSER_INSTALL "composer install --no-suggest --prefer-dist --no-interaction --no-progress"
ENV DRUPAL_ADMIN_ACCOUNT_NAME admin
ENV DRUPAL_CONFIGURATION_DIR ${APP_ROOT}/configuration
ENV DRUPAL_ROOT $APP_WEBROOT
ENV DRUPAL_SITE_ID defaultd
ENV DRUPAL_SITE_UUID FALSE
ENV DRUPAL_TESTING_ROOT ${APP_ROOT}/tests
ENV DRUPAL_TESTING_TOOLS FALSE
ENV DRUPAL_CHOWN_PUBLIC_FILES_STARTUP FALSE
ENV DRUPAL_UNIT_TEST_MODULES ''
ENV DRUSH "doas -u ${NGINX_RUN_USER} -- /app/html/vendor/bin/drush --root=${DRUPAL_ROOT} --uri=default --yes"
ENV DRUSH_PHP /usr/bin/php

ENV RSYNC_FLAGS --quiet
ENV RSYNC_COPY "rsync -a --inplace --no-compress ${RSYNC_FLAGS}"
ENV RSYNC_MOVE "${RSYNC_COPY} --remove-source-files"

ENV TERM dumb

# Install required packages, libraries.
COPY ./build /build
RUN apk --no-cache add \
    doas \
    git \
    mysql-client \
    php7-ctype \
    php7-dom \
    php7-dom \
    php7-fileinfo \
    php7-gd \
    php7-mbstring \
    php7-mysqlnd \
    php7-opcache \
    php7-pcntl \
    php7-pdo \
    php7-pdo_mysql \
    php7-posix \
    php7-session \
    php7-simplexml \
    php7-tokenizer \
    php7-xml \
    php7-xmlwriter \
    redis \
    rsync \
    sudo \
    unzip && \
  ${RSYNC_MOVE} /build/scripts/ /scripts/ && \
  ${RSYNC_MOVE} /build/data/htaccess/ /security_htaccess && \
  /scripts/setupDoasConf.sh && \
  composer global require hirak/prestissimo zaporylie/composer-drupal-optimizations:^1.1.2 --prefer-dist --no-interaction --update-no-dev && \
  apk --no-cache add yq --repository=http://dl-cdn.alpinelinux.org/alpine/v3.13/community/ && \
  /scripts/linkDrupalCronEntryInit.sh && \
  rm -rf ~/.composer/cache

# Volumes
VOLUME /app/html/sites/default
