FROM ubuntu:16.04
MAINTAINER Christian Lück <christian@lueck.tv>

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y php7.0-mbstring \
  git nginx supervisor php7.0-fpm php7.0-cli php7.0-curl php7.0-gd php7.0-json php-gettext php7.0-intl \
  php7.0-pgsql php7.0-ldap php7.0-mysql && apt-get clean && rm -rf /var/lib/apt/lists/*

# add ttrss as the only nginx site
ADD ttrss.nginx.conf /etc/nginx/sites-available/ttrss
RUN ln -s /etc/nginx/sites-available/ttrss /etc/nginx/sites-enabled/ttrss
RUN rm /etc/nginx/sites-enabled/default

ARG TTRSS_VERSION=7e2fd9bdce4a0ff05e7c76aee52e30c26d5b2093

# install ttrss and patch configuration
WORKDIR /var/www
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/* \
    && curl -SL https://git.tt-rss.org/fox/tt-rss/archive/${TTRSS_VERSION}.tar.gz | tar xzC /var/www --strip-components 1 \
    && apt-get purge -y --auto-remove curl \
    && chown www-data:www-data -R /var/www

ADD af_newspapers /var/www/plugins/af_newspapers

RUN git clone https://github.com/hydrian/TTRSS-Auth-LDAP.git /root/TTRSS-Auth-LDAP \
    && cp -r /root/TTRSS-Auth-LDAP/plugins/auth_ldap plugins/ \
    && rm -rf /root/TTRSS-Auth-LDAP \
    && git clone https://github.com/HenryQW/mercury_fulltext.git /var/www/plugins/mercury_fulltext \
    && ls -la /var/www/plugins

RUN cp config.php-dist config.php \
    && mkdir -p /var/run/php

# expose only nginx HTTP port
EXPOSE 80

# complete path to ttrss
ENV SELF_URL_PATH http://localhost

# expose default database credentials via ENV in order to ease overwriting
ENV DB_NAME ttrss
ENV DB_USER ttrss
ENV DB_PASS ttrss

# auth method, options are: internal, ldap
ENV AUTH_METHOD internal

# always re-configure database with current ENV when RUNning container, then monitor all services
ADD configure-db.php /configure-db.php
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
