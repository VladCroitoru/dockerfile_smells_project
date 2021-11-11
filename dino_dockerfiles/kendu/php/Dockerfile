################################################################################
#                                                                              #
#                                 {o,o}                                        #
#                                 |)__)                                        #
#                                 -"-"-                                        #
#                                                                              #
################################################################################
#
# The php-fpm container
#
#################################---INFO---#####################################

FROM ubuntu:latest
MAINTAINER Kendu <devops@kendu.si>

################################################################################

#################################---ENV---######################################

ENV DEBIAN_FRONTEND noninteractive

################################################################################

################################---BUILD---#####################################

RUN locale-gen sl_SI.UTF-8
# Use Ondřej Surý's PHP 5.6 packages
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main  " \
       > /etc/apt/sources.list.d/ondrej.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C
RUN apt-get update; \
    apt-get upgrade -y; \
    apt-get -y install \
        php5.6 \
        php5.6-fpm \
        php5.6-common \
        php5.6-curl \
        php5.6-gmp \
        php5.6-imagick \
        php5.6-intl \
        php5.6-json \
        php5.6-xml \
        php5.6-mcrypt \
        php5.6-memcache \
        php5.6-mongo \
        php5.6-pgsql \
        php5.6-mysql \
        php5.6-readline \
        php5.6-sqlite \
        php5.6-xdebug \
        php5.6-gd \
        php5.6-mbstring \
        php5.6-soap \
        wget \
        git \
        php5.6-cli \
        php5.6-readline \
    && \
    apt-get clean

RUN phpenmod mcrypt; \
    mkdir /run/php
WORKDIR /opt/web

################################################################################

#################################---EXPOSE---###################################

EXPOSE 9000

################################################################################

#################################---CMD---######################################

CMD php-fpm5.6 -F --fpm-config=/etc/php/5.6/fpm/php-fpm.conf \
             --force-stderr \
             -c /etc/php/5.6/fpm/php.ini

################################################################################
