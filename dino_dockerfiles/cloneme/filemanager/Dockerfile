# -----------------------------------------------------------------------------
# docker-filemanager
#
# Builds a basic docker image that can run a FileManager
# (https://github.com/simogeo/Filemanager).
#
# Authors: LM, BS
# Updated: February 12rd, 2016
# Require: Docker 1.9.1 (http://www.docker.io/)
# Done on Windobe !
# -----------------------------------------------------------------------------
FROM debian:jessie
MAINTAINER LM, Kelvin Chen <kelvin@kelvinchen.org>

# Install all dependencies that are used in multiple images.
RUN echo "deb http://httpredir.debian.org/debian jessie non-free" \
        >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
        vim \
        ca-certificates \
        python \
        python-dev \
        curl \
        git \
        nginx \
        unzip \
        unrar \
        supervisor \
        bzip2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        php5-fpm \
        php5-cli \
        php5-gd \
    && apt-get install --no-install-recommends -y apache2-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Download and install Filemanager
# Issue with github - easily fixeable
# ADD "https://github.com/simogeo/Filemanager/archive/master.zip" ./
ADD https://codeload.github.com/simogeo/Filemanager/zip/master /Filemanager-master.zip
RUN unzip Filemanager-master.zip -d /opt/;  rm /Filemanager-master.zip

# configure supervisor
ADD supervisord.conf /etc/supervisor/conf.d/

# Load in all of our config files.
COPY nginx.conf /etc/nginx/
#Given config file (filemanager.config.json) does not exist !
COPY filemanager.config.js "/opt/Filemanager-master/scripts/filemanager.config.json"

# Increase the upload file size limit
RUN sed -i 's/upload_max_filesize/;upload_max_filesize/g' /etc/php5/cli/php.ini 

# Unlock memory limit to allow large zip upload
RUN sed -i 's/memory_limit = 128M/memory_limit = -1/g' /etc/php5/fpm/php.ini

# /start runs it.
EXPOSE 80

VOLUME /downloads

CMD ["supervisord"]
