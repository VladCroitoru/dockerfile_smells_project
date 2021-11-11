# Version: 0.0.1
FROM debian:jessie

MAINTAINER Igor Savenko "bliss@cloudlinux.com"

ENV NGINX_VERSION 1.11.5-1~jessie

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
    && echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
    && apt-get update -q && DEBIAN_FRONTEND=noninteractive apt-get install \
    --no-install-recommends --no-install-suggests -y \
                                        ca-certificates \
                                        nginx=${NGINX_VERSION} \
                                        gettext-base \
                                        runit \
                                        curl \
    && rm -rf /var/lib/apt/lists/* \
    && sed -i -e "s/keepalive_timeout\s*65/keepalive_timeout 15/" \
              -e "/keepalive_timeout/a \\\tclient_max_body_size 100m;" \
              -e '/^user/ {s/nginx/www-data/}' \
              -e "/worker_processes/a daemon off;" /etc/nginx/nginx.conf \
    && rm -f /etc/nginx/conf.d/default.conf

RUN set -xe \
    && apt-get update -q && DEBIAN_FRONTEND=noninteractive apt-get install \
    --no-install-recommends --no-install-suggests -y \
                                            php5 \
                                            php5-mcrypt \
                                            php5-mysql \
                                            php5-fpm \
                                            php5-gd \
                                            php5-curl \
                                            php5-cli \
                                            php5-imap \
                                            unzip \
                                            cron \
                                            mysql-client \
                                            file \
    && rm -rf /var/lib/apt/lists/* \
    && sed -i -e "s/;\?cgi.fix_pathinfo\s*=\s*1/cgi.fix_pathinfo = 0/" \
    -e "s/;\?upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/" \
    -e "s/;\?max_execution_time\s*=\s*30/max_execution_time = 300/" \
    -e "s/;\?post_max_size\s*=\s*8M/post_max_size = 100M/" /etc/php5/fpm/php.ini \
    && sed -i -e "s/;\?daemonize\s*=\s*yes/daemonize = no/" /etc/php5/fpm/php-fpm.conf \
    && sed -i -e "s/;\?catch_workers_output\s*=\s*yes/catch_workers_output = yes/" \
    -e "/^pm/ {s/dynamic/ondemand/}" \
    -e "/^pm.max_children/ {s/5/3/}" \
    -e "/^pm.max_requests/ {s/500/200/}" \
    -e "/^;\?php_admin_value\[memory_limit\]/ {s/^;\?\(.*\)[[:digit:]]\{2,\}M$/\1256M/}" /etc/php5/fpm/pool.d/www.conf

COPY conf/default.conf /etc/nginx/conf.d

RUN set -x \
    && curl -o /tmp/ioncube.tar.gz http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64_5.1.2.tar.gz \
    && tar -zxf /tmp/ioncube.tar.gz -C /tmp \
    && if [ ! -d /usr/local/ioncube ];then mkdir /usr/local/ioncube; fi \
    && cp /tmp/ioncube/ioncube_loader_lin_5.6.so /usr/local/ioncube \
    && echo zend_extension = /usr/local/ioncube/ioncube_loader_lin_5.6.so >> /etc/php5/cli/php.ini \
    && echo zend_extension = /usr/local/ioncube/ioncube_loader_lin_5.6.so >> /etc/php5/fpm/php.ini \
    && rm -f /tmp/ioncube.tar.gz \
    && rm -rf /tmp/ioncube

COPY whmcs.sql /
RUN test -d /var/opt/whmcs || mkdir -p /var/opt/whmcs
RUN test -d /var/opt/persistent || mkdir -p /var/opt/persistent
COPY src/whmcs*.zip /

COPY service/ /etc/service

COPY runit-docker_1.1_amd64.deb /
RUN dpkg -i /runit-docker_1.1_amd64.deb && rm -f /runit-docker_1.1_amd64.deb

COPY scripts/loghandler.php /
COPY scripts/preset.php /
COPY scripts/reset.php /
COPY scripts/dbdump.sh /
COPY scripts/dbload.sh /

WORKDIR /var/opt/whmcs

VOLUME ["/var/opt/persistent"]

EXPOSE 80 443

CMD ["/sbin/runit-docker"]