FROM phusion/baseimage:0.9.18

MAINTAINER Bo-Yi Wu <appleboy.tw@gmail.com>

# Default baseimage settings
ENV HOME /root
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
CMD ["/sbin/my_init"]
ENV DEBIAN_FRONTEND noninteractive

# Add the PPA for PHP 5.6
RUN add-apt-repository ppa:ondrej/php5-5.6 -y

# Update software list and install php + nginx
RUN apt-get update \
  && apt-get install -y --force-yes \
  php5 \
  php5-fpm \
  php5-cli \
  php5-mysql \
  php5-mcrypt \
  php5-curl \
  php5-gd \
  php5-intl \
  mysql-client

# Clear cache
RUN apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  /tmp/* \
  /var/tmp/*

# Configure nginx
RUN mkdir -p /var/www

# Configure PHP
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = Asia\/Taipei/" /etc/php5/fpm/php.ini
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/cli/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = Asia\/Taipei/" /etc/php5/cli/php.ini
RUN php5enmod mcrypt

# clear cache.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add nginx volumes
VOLUME ["/var/www"]

# Set the work directory
WORKDIR /var/www
