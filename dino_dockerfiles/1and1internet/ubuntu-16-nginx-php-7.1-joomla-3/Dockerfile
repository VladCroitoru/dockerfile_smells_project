FROM 1and1internet/ubuntu-16-nginx-php-7.1:latest
MAINTAINER brian.wojtczak@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive

COPY files/ /

# Environment variables for the MySQL DB
ENV JOOMLA_DB_HOST=mysql \
    JOOMLA_DB_USER=username \
    JOOMLA_DB_NAME=databasename \
    JOOMLA_DB_PASSWORD=EnvVarHere

RUN \
    apt-get update &&\
    apt-get install -y zip unzip libmcrypt-dev libpng12-dev libjpeg-dev php7.1-gd php7.1-mysql curl &&\
    rm -rf /var/lib/apt/lists/* &&\
    JOOMLA_DOWNLOAD=https://downloads.joomla.org$(curl -fsL https://downloads.joomla.org/latest | grep -iEo '/cms/joomla3/.*-stable-full_package[-\.]tar[-\.]gz\?format=gz' | sort -nr | uniq | head -1) && \
    echo "Downloading from $JOOMLA_DOWNLOAD" && \
    curl -fsL $JOOMLA_DOWNLOAD -o /usr/src/joomla.tar.gz && \
    sha1sum /usr/src/joomla.tar.gz && \
    chmod -R 755 /hooks /init && \
    chmod 666 /etc/nginx/sites-enabled/site.conf
