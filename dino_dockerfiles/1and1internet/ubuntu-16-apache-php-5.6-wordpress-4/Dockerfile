FROM 1and1internet/ubuntu-16-apache-php-5.6:latest
MAINTAINER james.wilkins@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive

COPY files/ /

# Environment variables for the MySQL DB
ENV WORDPRESS_DB_HOST=mysql \
    WORDPRESS_DB_USER=username \
    WORDPRESS_DB_NAME=databasename \
    WORDPRESS_DB_PASSWORD=EnvVarHere \
    WORDPRESS_DB_PREFIX='wp_'

RUN \
apt-get update &&\
apt-get install -y unzip libpng12-dev libjpeg-dev php5.6-gd php5.6-mysql curl &&\
rm -rf /var/lib/apt/lists/* &&\
a2enmod rewrite expires &&\
{ \
    echo 'opcache.memory_consumption=128'; \
    echo 'opcache.interned_strings_buffer=8'; \
    echo 'opcache.max_accelerated_files=4000'; \
    echo 'opcache.revalidate_freq=60'; \
    echo 'opcache.fast_shutdown=1'; \
    echo 'opcache.enable_cli=1'; \
  } > /etc/php/5.6/apache2/conf.d/10-opcache.ini && \
#curl -o /usr/src/wordpress.tar.gz -fSL https://wordpress.org/latest.tar.gz &&\
WORDPRESS_DOWNLOAD=$(curl -fsL https://wordpress.org/download/release-archive/ | grep -Eo 'https://wordpress.org/wordpress-4.[0-9]{1,2}.[0-9]{1,2}.tar.gz' | sort -nr | uniq | head -1) && \
curl -fsL $WORDPRESS_DOWNLOAD -o /usr/src/wordpress.tar.gz && \
chmod -R 755 /hooks /init
