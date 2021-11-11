FROM 1and1internet/ubuntu-16-nginx-php-5.6:latest
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
WORDPRESS_DOWNLOAD=$(curl -fsL https://wordpress.org/download/release-archive/ | grep -Eo 'https://wordpress.org/wordpress-4.[0-9\.]{1,4}.tar.gz' | head -1) && \
curl -fsL $WORDPRESS_DOWNLOAD -o /usr/src/wordpress.tar.gz && \
chmod -R 755 /hooks /init && \
chmod 666 /etc/nginx/sites-enabled/site.conf
