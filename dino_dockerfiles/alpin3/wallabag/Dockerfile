FROM alpin3/php-apache:3.4
MAINTAINER kost - https://github.com/kost

ENV WALLABAG_VERSION=2.1.4 \
    WALLABAG_SECRET=ovmpmAWXRCabNlMgzlzFXDYmCFfzGv \
    WALLABAG_SMTPHOST=127.0.0.1 \
    WALLABAG_SMTPUSER=null \
    WALLABAG_SMTPPASSWORD=null \
    WALLABAG_SMTPFROM=no-reply@example.org \
    SYMFONY_ENV=prod

RUN apk upgrade --no-cache --update && apk --update --no-cache add wget ca-certificates \
      curl \
      git \
      tar \
      libwebp \
      mariadb-client \
      postgresql-client \
      pcre \
      php5 \
      php5-bcmath \
      php5-ctype \
      php5-curl \
      php5-dom \
      php5-fpm \
      php5-gd \
      php5-gettext \
      php5-iconv \
      php5-json \
      php5-openssl \
      php5-pdo_mysql \
      php5-pdo_pgsql \
      php5-pdo_sqlite \
      php5-phar \
      php5-xml \
      php5-zlib \
      php5\
      py-mysqldb \
      py-psycopg2 \
      py-simplejson \
    && mkdir /web \
    && git clone --branch $WALLABAG_VERSION --depth 1 https://github.com/wallabag/wallabag.git /web/wallabag \
    && cd /web/wallabag \
    && echo "Success"

COPY root /

RUN cd /web/wallabag \
    && composer install --no-dev -o --prefer-dist \
    && chown -R apache:apache var bin app/config vendor data web \
#    && ln -sf /dev/stdout /web/wallabag/var/logs/$SYMFONY_ENV-test.log \
    && echo "Success"

ADD scripts/ /scripts

VOLUME ["/web/wallabag/var","/web/wallabag/data","/web/wallabag/config"]
