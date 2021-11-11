FROM ubuntu:20.04

LABEL name="wordpress docker container" \
     version="5.8.1"

ARG DEBIAN_FRONTEND=noninteractive

ARG DUMB_INIT_VERSION=1.2.5
ARG WP_CLI_VERSION=2.4.0
ARG WP_CORE_VERSION=5.8.1
ARG WP_PLUGIN_OFFLOAD_S3_VERSION=2.5.5
ARG WP_PLUGIN_OFFLOAD_SES_VERSION=1.4.6
ARG WP_SCRIPTS_VERSION=0.14

ENV MYSQL_DATABASE=wordpress \
    MYSQL_HOST=localhost \
    MYSQL_PORT=3306 \
    MYSQL_USER=root \
    MYSQL_PASSWORD=secret \
    REDIS_HOST=localhost \
    REDIS_PORT=6379 \
    WP_CLI_PACKAGES_DIR=/opt/wp-cli-packages \
    WP_S3_MIGRATOR_VERSION=2.3.2


RUN apt-get update && apt-get install -y \
    php-xml \
    php-xmlrpc \
    php-curl \
    php-intl \
    php-mbstring \
    php-gd \
    php-zip \
    php-mysql \
    php-redis \
    php-opcache \
    php-fpm \
    php-soap \
    php-imagick \
    nginx \
    wget \
    unzip \
    sudo \
    curl \
    bats \
    less \
    mysql-client && \
    apt-get upgrade -y && \
    apt-get clean

ADD det-arch.sh /usr/local/bin
RUN wget https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_`/usr/local/bin/det-arch.sh a r`.deb && \
    dpkg -i dumb-init_*.deb && rm dumb-init_*.deb

RUN wget -q https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod 755 wp-cli.phar && mv wp-cli.phar /usr/local/bin/wp && \
    mkdir /app && \
    cd /app && \
    /usr/local/bin/wp core download --allow-root --locale=de_DE && \
    wget -q https://downloads.wordpress.org/plugin/amazon-s3-and-cloudfront.zip && \
    unzip amazon-s3-and-cloudfront.zip && \
    mv amazon-s3-and-cloudfront /app/wp-content/plugins && \
    rm amazon-s3-and-cloudfront.zip && \
    wget -q https://downloads.wordpress.org/plugin/wp-ses.zip && \
    unzip wp-ses.zip && \
    mv wp-ses /app/wp-content/plugins && \
    rm wp-ses.zip && \
    mkdir -p /app/wp-content/languages && \
    cd /app/wp-content/languages && \
    chown -R www-data /var/lib/nginx && \
    mkdir -p /app/wp-content/uploads && \
    chown -R www-data /app/wp-content/uploads

RUN wget -q https://github.com/arvatoaws-labs/wp-scripts/archive/${WP_SCRIPTS_VERSION}.zip && \
  unzip ${WP_SCRIPTS_VERSION}.zip && \
  mv wp-scripts* /scripts && \
  rm ${WP_SCRIPTS_VERSION}.zip && \
  mkdir -p WP_CLI_PACKAGES_DIR && \
  wp package install arvatoaws-labs/wp-arvato-aws-s3-migrator:${WP_S3_MIGRATOR_VERSION} --allow-root

WORKDIR /app

COPY src/wp-config.php /app/wp-config.php
COPY src/amazon-s3-and-cloudfront-tweaks.php /app/wp-content/plugins/amazon-s3-and-cloudfront-tweaks.php
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/fpm.conf /etc/php/7.4/fpm/php-fpm.conf
COPY conf/fpm-pool.conf /etc/php/7.4/fpm/pool.d/www.conf

RUN chmod 755 /scripts/*.sh

ENTRYPOINT ["/usr/bin/dumb-init", "--"]

USER www-data
