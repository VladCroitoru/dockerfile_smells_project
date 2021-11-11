FROM debian:wheezy
MAINTAINER Tibor Sári <tiborsari@gmx.de>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y

# install php and apache and clean up to minimize the image size
RUN echo "deb http://packages.dotdeb.org wheezy all" >> /etc/apt/source.list && \
    echo "deb-src http://packages.dotdeb.org wheezy all" >> /etc/apt/source.list && \
    apt-get install -y wget && \
    wget http://www.dotdeb.org/dotdeb.gpg && \
    apt-key add dotdeb.gpg && \
    apt-get update -qq && apt-get install --no-install-recommends -y \
        apache2 \
        curl \
        libapache2-mod-php5 \
        php5-cli \
        php5-mysql \
        php5-curl \
        php5-memcache \
        php5-memcached \
        php5-mcrypt \
        libssh2-php \
        supervisor \
        sudo \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm -rf /var/www && \
    mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/httpdocs /var/www/log && \
    chown -R www-data:www-data /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www && \
    chmod 777 /var/www/log

# Apache + PHP requires preforking Apache for best results
RUN a2enmod rewrite && a2enmod php5
RUN a2enmod rewrite && a2enmod php5

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Update the default apache site with the config we created.
COPY apache2/apache2.conf /etc/apache2/sites-enabled/000-default
COPY apache2/ports.conf /etc/apache2/ports.conf

EXPOSE 80

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]