FROM centos:5.11
MAINTAINER Huttopia <dev@huttopia.com>

# Install Requirements
RUN yum update -y \
    && yum install -y \
        sudo \
        wget \
        curl \
        git \
        apt-utils \
        acl \
        gcc \
        gcc-c++ \
        autoconf \
        automake \
        make \
    && echo "Europe/Paris" > /etc/localtime && yum search -y tzdata && yum update -y tzdata \
    && echo 'alias ll="ls -lah --color=auto"' >> /etc/bash.bashrc

# Install PHP & Apache
RUN yum update -y \
    && yum install -y \
        php-mysql \
        php-pear \
        php-mbstring \
        php-devel \
        curl-devel \
        httpd-devel \
        pcre-devel \
        php-xml

# Update PHP PEAR
RUN pear channel-update pear.php.net \
    && pear upgrade --force PEAR-1.5.0 \
    && cd /tmp \
    && wget http://download.pear.php.net/package/Structures_Graph-1.0.4.tgz \
    && tar xvzf Structures_Graph-1.0.4.tgz \
    && mv /tmp/Structures_Graph-1.0.4/Structures /usr/share/pear/Structures \
    && rm -f /tmp/Structures_Graph-1.0.4.tgz \
    && rm -rf /tmp/Structures_Graph-1.0.4

# Config PHP PEAR
RUN sed -i "s/<?php/<?php ini_set ('memory_limit', '16M');/g" /usr/share/pear/pearcmd.php

# Install Packages PECL
RUN pecl channel-update pecl.php.net \
    && pecl install \
        apc \
        json \
        pecl_http-1.7.6 \
        xdebug-2.0.0

# Install Packages PEAR
RUN pear install \
        OLE-1.0.0RC2 \
        Spreadsheet_Excel_Writer-0.9.3 \
        Date \
        Calendar-0.5.5 \
        XML_Parser \
        XML_Util \
        XML_Serializer-0.20.2

# Config Apache
RUN mkdir /etc/httpd/sites-enabled
ADD assets/conf/httpd.conf /etc/httpd/conf/httpd.conf

# Config PHP
ADD assets/conf/php.ini /etc/php.ini

# Sources
WORKDIR /var/www

EXPOSE 80

VOLUME ["/var/www", "/etc/httpd/sites-enabled"]

# Start
ADD assets/start /bin/start
RUN chmod +x /bin/start

CMD ["bash", "start"]