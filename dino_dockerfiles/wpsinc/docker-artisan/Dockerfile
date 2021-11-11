FROM debian:jessie

MAINTAINER "WPS" <web_services@wps-inc.com>

WORKDIR /tmp

RUN apt-get update && apt-get install -y \
    php5-cli \
    php5-curl \
    php5-gd \
    php5-mcrypt \
    php5-mongo \
    php5-mssql \
    php5-mysqlnd \
    php5-pgsql \
    php5-redis \
    php5-sqlite

# Cleanup
RUN apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /var/www/html

WORKDIR /var/www/html

ENTRYPOINT ["php", "artisan"]

CMD ["--help"]
