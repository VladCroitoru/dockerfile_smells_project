FROM centos:6.6

MAINTAINER "Jean Lalande" <jeanlalande@gmail.com>

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/httpd
ENV APACHE_LOCK_DIR /var/lock/httpd
ENV APACHE_PID_FILE /var/run/httpd.pid

RUN yum -y update
RUN yum -y install httpd php php-cli php-gd php-mbstring php-mysql php-pear

RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php.ini
RUN sed -i "s/#ServerName.*/ServerName localhost/" /etc/httpd/conf/httpd.conf

# Composer Installation
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Startup script
ADD scripts/run.sh /run.sh
RUN chmod 755 /run.sh

# Apache configuration & sample app
ADD sample /var/www/site
ADD apache-config.conf /etc/httpd/conf.d/000-default.conf

EXPOSE 80

WORKDIR /var/www/site

CMD ["/run.sh"]
