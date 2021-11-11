FROM php:5.6-apache
MAINTAINER Cyril MOREAU <cyril.moreauu@gmail.com>

# ONBUILD directives took care of uploading
# the code and install dependencies

RUN rm /etc/apache2/mods-available/php5.load
RUN    apt-get -qq update && \
    apt-get install -qqy php5-mysql && \
    apt-get install -qqy  php5-pgsql && \
    apt-get install -qqy php5-gd && \
    apt-get install -qqy php5-imap && \
    apt-get install -y libapache2-mod-php5 && \
    apt-get clean 


# Install entry-point script
ADD php.ini /etc/php5/apache2/php.ini
COPY projeqtorV5.1.5 /var/www/html/
RUN chown -R www-data:www-data /var/www/html
