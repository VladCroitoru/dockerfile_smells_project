FROM ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
        apt-get -y install \
        php-pear \
        php7.0 \
        php7.0-cgi \
        php7.0-cli \
        php7.0-common \
        php7.0-curl \
        php7.0-dev \
        php7.0-gd \
        php7.0-intl \
        php7.0-mcrypt \
        php7.0-mbstring \
        php7.0-xmlrpc \
        php7.0-mysql \
        php7.0-pgsql \
        php7.0-fpm \
        php7.0-zip \
        php7.0-ldap \
        php7.0-soap \
        unzip \
        apt-transport-https \
        unixodbc-dev \
        build-essential \
        libaio1 \
				locales \
        autoconf && apt-get clean

RUN echo "en_US.UTF-8 UTF-8\nen_AU.UTF-8 UTF-8" > /etc/locale.gen
RUN locale-gen
RUN mkdir -p /var/moodle/moodledata /var/moodle/phpunitdata /var/moodle/behatdata
WORKDIR /usr/src

RUN mkdir -p /var/moodle/moodledata /var/moodle/phpunitdata /var/moodle/behatdata

WORKDIR /usr/src
CMD php-fpm7.0 -R
