FROM 1and1internet/ubuntu-16-apache-php-5.6:latest
MAINTAINER james.poole@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
ENV DRUPAL_DB_HOST=mysql \
    DRUPAL_DB_PORT=3306 \
    DRUPAL_DB_USER=drupal \
    DRUPAL_DB_NAME=drupal \
    DRUPAL_DB_PASSWORD=EnvVarHere \
    DRUPAL_DB_DRIVER=mysql \
    DRUPAL_DB_PREFIX=''
RUN \
    apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev drush php-uploadprogress && \
    rm -rf /var/lib/apt/lists/* && \
    DRUPAL_VERSION=$(curl -fsl https://www.drupal.org/node/3060/release/feed.xml | grep -Eo 'drupal/releases/8.[0-9]{1,4}.[0-9]{1,4}"' | sort -nr | head  -1 | awk -F'/' '{ print $3 }' | sed 's/\([^"]*\)./\1/') && \
    echo "Pulling drupal-${DRUPAL_VERSION}" && \
    curl -fSL "https://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o /usr/src/drupal.tar.gz && \
    chmod -R 755 /hooks /init
    
