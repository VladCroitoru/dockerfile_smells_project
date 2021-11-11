FROM davask/d-base:latest
MAINTAINER davask <contact@davaskweblimited.com>

LABEL dwl.server.http="apache2"

RUN apt-get update
RUN apt-get install -y apache2
RUN apt-get install -y apache2-utils
RUN rm -rf /var/lib/apt/lists/*

RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf && a2enconf fqdn

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

# Configure apache
RUN a2enmod rewrite
RUN a2enmod expires
RUN a2enmod headers
RUN a2enmod cgi

# proxy protection
RUN a2enmod remoteip

VOLUME /etc/apache2/sites-enabled

EXPOSE 80

# Declare instantiation counter
ENV DWL_INIT_COUNT 1

# Copy instantiation specific file
COPY ./apache2.sh $DWL_INIT_DIR/$DWL_INIT_COUNT-apache2.sh
