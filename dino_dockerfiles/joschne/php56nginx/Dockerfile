## Github URL: https://github.com/LaraDock/docker-images/tree/master/phpnginx
## Docker URL: https://hub.docker.com/r/laradock/phpnginx
#############################################################################
FROM phusion/baseimage:0.9.17

MAINTAINER Mahmoud Zalt <mahmoud@zalt.me>
# INSPIRED BY github.com/LaraDock/docker-images/phpnginx

# Default baseimage settings
ENV HOME /root
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh
CMD ["/sbin/my_init"]
ENV DEBIAN_FRONTEND noninteractive

RUN add-apt-repository ppa:ondrej/php5-5.6 -y

RUN apt-get update \
    && apt-get install -y --force-yes \
    nginx \
    php5 \
    php5-fpm \
    php5-cli \
    php5-mysql \
    php5-pgsql \
    php5-mcrypt \
    php5-curl \
    php5-gd \
    php5-intl \
    php5-xdebug \
    php5-xsl


RUN apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
              /tmp/* \
              /var/tmp/*

# Configure nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN sed -i "s/sendfile on/sendfile off/" /etc/nginx/nginx.conf
RUN mkdir -p /var/www

# Configure PHP
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = Europe\/Paris/" /etc/php5/fpm/php.ini
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/cli/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = Europe\/Paris/" /etc/php5/cli/php.ini
RUN php5enmod mcrypt

# Configure PHP to enable XDebug
RUN touch /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "zend_extension = xdebug.so" >> /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "xdebug.remote_host = 172.17.0.1" >> /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "xdebug.default_enable = 1" >> /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "xdebug.remote_enable = on" >> /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "xdebug.remote_port = 9000" >> /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "xdebug.remote_connect_back = On" >> /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "xdebug.remote_handler = dbgp" >> /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "xdebug.profiler_enable = 0" >> /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "xdebug.profiler_output_dir = \"/var/log\"" >> /etc/php5/fpm/conf.d/40-custom.ini
RUN echo "xdebug.remote_log = \"/var/www/log\"" >> /etc/php5/fpm/conf.d/40-custom.ini


# Add nginx service
RUN mkdir /etc/service/nginx
ADD build/nginx/run.sh /etc/service/nginx/run
RUN chmod +x /etc/service/nginx/run

# Add PHP service
RUN mkdir /etc/service/phpfpm
ADD build/php/run.sh /etc/service/phpfpm/run
RUN chmod +x /etc/service/phpfpm/run

VOLUME ["/var/www", "/etc/nginx/sites-available", "/etc/nginx/sites-enabled"]

WORKDIR /var/www

EXPOSE 80 9000
