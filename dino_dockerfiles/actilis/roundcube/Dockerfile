FROM actilis/httpd-php:debian-apache
EXPOSE 80

MAINTAINER Francois MICAUX <dok-images@actilis.net> 

LABEL Vendor="Actilis" \
      License="GPLv3" \
      Version="2018.12.30"

ENV RC_VERSION=1.3.8
ENV RC_URL=https://github.com/roundcube/roundcubemail/releases/download/${RC_VERSION}/roundcubemail-${RC_VERSION}-complete.tar.gz

RUN rm -rf /var/www/html/* 
WORKDIR /var/www/html

# Install Roundcube and configure Composer
# Adjust Composer config : stability to dev for some requirements
RUN echo Download ${RC_URL} &&  curl -SL ${RC_URL} | tar -C /var/www/html -xz --strip-components 1 \
 && mkdir -p /var/www/html/plugins/thunderbird_labels \
 && rm -rf /var/www/html/installer \
 && head -n -2 composer.json-dist > composer.json \
 && sed -i -e '$a\    },\n    "minimum-stability": "dev",\n    "prefer-stable": true\n}' composer.json \
 && ls -l 

# Run Composer requirements
RUN COMPOSER_ALLOW_SUPERUSER=1 composer -n require \
      pear/console_commandline \
      phpunit/php-code-coverage:4.0.x-dev \
      phpunit/php-token-stream:2.0.X-dev \
      johndoh/contextmenu \
      weird-birds/thunderbird_labels \
      cor/message_highlight \
      prodrigestivill/gravatar 

# Plugins : Kolab
RUN COMPOSER_ALLOW_SUPERUSER=1 composer -n require  kolab/libcalendaring kolab/calendar 

# Carddav, but no CalDAV... (http://www.roundcubeforum.net/index.php/topic,24189.0.html)
# NEEDS PHP<7 # RUN composer -n require roundcube/carddav
# NEEDS PHP<7 # COPY files/carddav-config.inc.php    /var/www/html/plugins/carddav/config.inc.php

# Plugins : dev / unstable
#RUN composer -n require melanie2/jquery_mobile melanie2/mobile melanie2/infinitescroll 
#RUN composer -n require takika/rc_smime
#RUN composer -n require stwa/google-addressbook sblaisot/automatic_addressbook 

# Configuration & initial db setup
COPY  files/defaults.inc.php  /var/www/html/config/defaults.inc.php
COPY  files/config.inc.tmpl   /var/www/html/config/config.inc.tmpl
COPY  files/entrypoint.sh     /rc-ep.sh
COPY  files/initial-db.sql    /tmp/initial-db.sql
COPY  files/bootstrap.php     /


# Entrypoint will call CMD from from httpd-php after taking care of parameters (env-vars)
ENTRYPOINT ["/rc-ep.sh"]
CMD ["apache2-foreground"]
