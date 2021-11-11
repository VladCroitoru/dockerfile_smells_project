FROM davask/d-apache2:2.4-u14.04
MAINTAINER davask <contact@davaskweblimited.com>
USER root
LABEL dwl.server.https="open ssl"

# declare container type
ENV DWL_INIT ssl

ENV APACHE_SSL_DIR /etc/apache2/ssl
ENV DWL_USER_DNS www.test.fr

# create apache2 ssl directories
RUN /bin/bash -c 'mkdir -p ${APACHE_SSL_DIR}'
# install certbot
RUN /bin/bash -c 'wget https://dl.eff.org/certbot-auto'
RUN /bin/bash -c 'mv certbot-auto /usr/local/sbin'
RUN /bin/bash -c 'chmod a+x /usr/local/sbin/certbot-auto'
# RUN /bin/bash -c 'echo 'y\n' | ./certbot-auto'
# /etc/letsencrypt/accounts
# https://letsencrypt.org/documents/LE-SA-v1.0.1-July-27-2015.pdf
# RUN /bin/bash -c 'certbot-auto certonly --webroot -w /var/www/html -d dev.davaskweblimited.com'

# Configure apache ssl
RUN /bin/bash -c 'a2enmod ssl'

# RUN printf 'FR\n.\nLyon\ndavask web limited\nIT\ndavaskweblimited.com\nadmin@davaskweblimited.com\n' | openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt

COPY ./etc/apache2/sites-enabled /etc/apache2/sites-enabled
COPY ./tmp/dwl/init.sh /tmp/dwl/init.sh
