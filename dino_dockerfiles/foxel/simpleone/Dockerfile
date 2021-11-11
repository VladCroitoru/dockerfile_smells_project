FROM ubuntu:16.04

MAINTAINER Andrey F. Kupreychik <foxel@quickfox.ru>

ENV DEBIAN_FRONTEND='noninteractive' \
  LANG='C.UTF-8'

RUN \
  apt-get update && \
  apt-get -y --no-install-recommends install \
    wget curl ca-certificates supervisor cron \
    nginx php7.0-cli php7.0-curl php7.0-fpm php7.0-gd \
    php7.0-mcrypt php7.0-mysql php7.0-xml php7.0-mbstring \
    php7.0-readline make default-jre-headless unzip && \
  rm -f /etc/php/7.0/fpm/pool.d/* /etc/nginx/sites-enabled/* && \
  rm -rf /etc/logrotate.d/* && \
  rm -rf /var/lib/apt/lists/*

COPY composer.json setup.sh /var/www/
RUN \
    cd /var/www && \
    bash ./setup.sh && \
    rm setup.sh composer.json

COPY core /var/www/core
COPY db /var/www/db
COPY lib /var/www/lib
COPY plugins /var/www/plugins
COPY static /var/www/static
COPY cron.php index.php ping.php Makefile /var/www/
COPY data/sone.qfc.php.sample /etc/simpleone/

RUN \
    mkdir /data && \
    cd /var/www && \
    ln -s /data ./data && \
    mkdir ./logs

# config
ADD docker/ /

RUN \
    chmod 0600 /etc/crontab && \
    chmod 0644 /etc/logrotate.d/* && \
    ln -s /etc/nginx/sites-available/simpleone.conf /etc/nginx/sites-enabled/simpleone.conf

EXPOSE 80

WORKDIR /var/www

VOLUME /data /var/www/logs /var/log

CMD ["/bin/start.sh"]
