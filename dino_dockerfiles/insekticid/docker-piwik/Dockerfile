FROM phpearth/php:7.3-nginx

MAINTAINER matomo@exploit.cz

ENV PHP_INI_DIR /etc/php/7.3
RUN mkdir -p $PHP_INI_DIR/conf.d && rm /etc/nginx/conf.d/default.conf 

RUN apk add --no-cache bash php7.3-gd php7.3-mbstring php7.3-intl php7.3-pdo_mysql php7.3-redis make gnupg composer php7.3-apcu

ENV MATOMO_VERSION 3.13.2

RUN curl -fsSL -o matomo.tar.gz \
      "https://builds.matomo.org/matomo-${MATOMO_VERSION}.tar.gz" \
 && curl -fsSL -o matomo.tar.gz.asc \
      "https://builds.matomo.org/matomo-${MATOMO_VERSION}.tar.gz.asc" \
 && export GNUPGHOME="$(mktemp -d)" \
 && gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys 814E346FA01A20DBB04B6807B5DBD5925590A237 \
 && gpg --batch --verify matomo.tar.gz.asc matomo.tar.gz \
 && rm -rf "$GNUPGHOME" 2>&1 \
 && rm -rf matomo.tar.gz.asc 2>&1 \
 && tar -xzf matomo.tar.gz -C /var/www/html \
 && rm -f matomo.tar.gz 2>&1

COPY php.ini /etc/php/7.3/conf.d/php.ini

RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php/7.3/php-fpm.d/www.conf && \
    sed -i -e "s/;pm.status_path = \/status/pm.status_path = \/status/g" /etc/php/7.3/php-fpm.d/www.conf && \
    sed -i -e "s/;ping.path = \/ping/ping.path = \/ping/g" /etc/php/7.3/php-fpm.d/www.conf && \
    sed -i -e "s/;clear_env = no/clear_env = no/g" /etc/php/7.3/php-fpm.d/www.conf && \
    sed -i -e "s/;ping.response = pong/ping.response = pong/g" /etc/php/7.3/php-fpm.d/www.conf
    #sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /etc/php/7.3/php-fpm.d/www.conf && \
    #sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /etc/php/7.3/php-fpm.d/www.conf && \
    #sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g" /etc/php/7.3/php-fpm.d/www.conf && \
    #sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g" /etc/php/7.3/php-fpm.d/www.conf && \
    #sed -i -e "s/pm.max_requests = 500/pm.max_requests = 1000/g" /etc/php/7.3/php-fpm.d/www.conf


#RUN set -ex; \
#    curl -fsSL -o GeoIPCity.tar.gz \
#        "https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz"; \
#    curl -fsSL -o GeoIPCity.tar.gz.md5 \
#        "https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz.md5"; \
#    echo "$(cat GeoIPCity.tar.gz.md5)  GeoIPCity.tar.gz" | md5sum -c -; \
#    mkdir -p /usr/src/GeoIPCity; \
#    tar -xf GeoIPCity.tar.gz -C /usr/src/GeoIPCity --strip-components=1; \
#    mv /usr/src/GeoIPCity/GeoLite2-City.mmdb /var/www/html/matomo/misc/GeoLite2-City.mmdb; \
#    rm -rf GeoIPCity*

COPY nginx.conf /etc/nginx/
COPY sites-available/* /etc/nginx/sites-available/
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

RUN chown -R www-data:www-data /var/www/html /var/tmp/nginx

WORKDIR /var/www/html/matomo

VOLUME /var/www/html/matomo

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

CMD ["/sbin/runit-wrapper"]

#EXPOSE 9000
