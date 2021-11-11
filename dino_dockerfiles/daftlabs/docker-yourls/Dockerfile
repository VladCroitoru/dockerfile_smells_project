FROM ubuntu:14.04

ENV APP_ROOT /yourls
ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p ${APP_ROOT} \
  && apt-get update \
  && apt-get install -y curl apache2 supervisor libapache2-mod-php5 php5-mysql \
  && unset DEBIAN_FRONTEND \
  && rm -rf /var/lib/apt/lists/* \
  && curl -L https://github.com/YOURLS/YOURLS/archive/1.7.1.tar.gz | tar -zx -C ${APP_ROOT} --strip-components=1 \
  && php5enmod mysql \
  && echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf \
  && a2enconf fqdn \
  && a2enmod php5 rewrite

COPY docker/start-yourls.sh /usr/bin/start-yourls.sh
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker/vhost.conf /etc/apache2/sites-enabled/000-default.conf
COPY docker/config.php ${APP_ROOT}/user/config.php
COPY docker/migrate.php ${APP_ROOT}/migrate.php
COPY docker/.htaccess ${APP_ROOT}/.htaccess
COPY docker/index.php ${APP_ROOT}/index.php

WORKDIR ${APP_ROOT}

RUN chown -R www-data:www-data ${APP_ROOT}

EXPOSE 80
CMD ["/usr/bin/supervisord"]
