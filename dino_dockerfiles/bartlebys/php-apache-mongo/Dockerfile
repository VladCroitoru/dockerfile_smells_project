FROM php:5.6-apache
MAINTAINER Benoit Pereira da Silva <https://pereira-da-silva.com>

###############
#   Mongo DB
###############

# Procedure from the official Mongo Doc.
# https://docs.mongodb.com/manual/tutorial/install- 
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list
RUN apt-get update
RUN apt-get install -y mongodb-org

#   **WARNING (Windows & OS X):*** from https://hub.docker.com/_/mongo/
#
#   The default Docker setup on Windows and OS X uses a VirtualBox VM to host the Docker daemon.
#   Unfortunately, the mechanism VirtualBox uses to share folders between the host system and the Docker container is not compatible with the memory mapped files used by MongoDB
#   (see vbox bug, docs.mongodb.org and related jira.mongodb.org bug).
#   This means that it is not possible to run a MongoDB container with the data directory mapped to the host.
#
#   The Docker documentation is a good starting point for understanding the different storage options and variations,
#   and there are multiple blogs and forum postings that discuss and give advice in this area.
#   We will simply show the basic procedure here for the latter option above:
#   Create a data directory on a suitable volume on your host system, e.g. /my/own/datadir.
#   Start your mongo container like this:
#
#   $  docker run --name some-mongo -v /my/own/datadir:/data/db -d mongo:tag
#   The -v /my/own/datadir:/data/db part of the command mounts the /my/own/datadir directory from the underlying host system as /data/db inside the container,
#   where MongoDB by default will write its data files.

RUN mkdir -p /data/db /data/configdb \
	&& chown -R mongodb:mongodb /data/db /data/configdb
VOLUME /data/db /data/configdb


###############
# Nano
###############

# We want to have a simple editor by default
RUN apt-get install nano


###############
#  Apache
###############

# Enable apache mods.
RUN a2enmod rewrite

################
#   PHP
################


#  NOTES https://hub.docker.com/_/php/
#
#  PHP Core Extensions :
#
#  For iconv, mcrypt and gd extensions, you can inherit the base image that you like, and write your own Dockerfile like this:
#
#   RUN apt-get update && apt-get install -y \
#           libfreetype6-dev \
#           libjpeg62-turbo-dev \
#           libmcrypt-dev \
#           libpng12-dev \
#      && docker-php-ext-install -j$(nproc) iconv mcrypt \
#      && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
#      && docker-php-ext-install -j$(nproc) gd
#
#
#  PECL : (compiling extension)
#
#
# To install a PECL extension, use "pecl install" to download and compile it,
# then use "docker-php-ext-enable" to enable it
#
# e.g : memcached
#
#   RUN apt-get update && apt-get install -y libmemcached-dev \
#       && pecl install memcached \
#       && docker-php-ext-enable memcached


# mcrypt
RUN apt-get install -y libmcrypt-dev
RUN docker-php-ext-install -j$(nproc) mcrypt

# iconv
RUN docker-php-ext-install -j$(nproc) iconv

# semaphore
RUN docker-php-ext-install -j$(nproc) sysvsem

# XDEBUG
# We install XDEBUG but do not enable it
# We enable it according to the context in Childrens
RUN yes | pecl install xdebug

# mongo

RUN apt-get install -y  libsasl2-dev\
                        libssl-dev

RUN pecl install mongo &&\
    echo "extension=mongo.so" > /usr/local/etc/php/conf.d/mongo.ini


# Install Telnet to be able to test the connectivity from the container to the host
RUN apt-get install telnet