# Latest Ubuntu LTS
FROM cloudposse/apache-php-fpm:latest

MAINTAINER  Erik Osterman "e@osterman.com"

ADD rootfs /

# Activate modules
RUN a2enmod vhost_alias

# Activate configurations
RUN a2enconf dynamic-vhost
 
