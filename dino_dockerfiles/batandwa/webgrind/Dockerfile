FROM phusion/baseimage:0.9.18
MAINTAINER Batandwa Colani <Batandwa.Colani@dstvdm.com>

RUN apt-get update
RUN apt-get install -y php5-common php5-cli apache2 php5 libapache2-mod-php5 php5-mcrypt
RUN apt-get install -y php5-curl php5-gd php5-ldap php5-imap \
    php5-odbc php5-memcached php5-xmlrpc php5-mcrypt php5-mysqlnd php5-xdebug curl \
    ImageMagick libxml2 memcached librabbitmq-dev librabbitmq1
RUN php5enmod mcrypt
RUN a2enmod rewrite

ENV APP_DOCUMENT_ROOT /var/www
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV DISABLE_CRON 1

VOLUME ['/var/www', '/var/log/apache2', '/etc/apache2', '/var/xdebug/profiler']

ADD docker_image/init.sh /etc/service/apache2/run
RUN chmod +x /etc/service/apache2/run
ADD docker_image/apache_site.conf /etc/apache2/sites-available/000-default.conf

ADD docker_image/custom_php.ini /etc/php5/mods-available/custom.ini
RUN php5enmod custom

RUN ln /var/log/syslog /var/log/apache2/error.log -sf
RUN ln /var/log/syslog /var/log/apache2/access.log -sf

# Get the code in.
RUN rm $APP_DOCUMENT_ROOT -rf
COPY . $APP_DOCUMENT_ROOT
