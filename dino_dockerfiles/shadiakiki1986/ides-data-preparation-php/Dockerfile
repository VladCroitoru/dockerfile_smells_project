FROM shadiakiki1986/php7-apache-odbc-and-other
MAINTAINER Shadi Akiki

# apache configs
WORKDIR /etc/apache2/sites-enabled
COPY etc/apache2/sites-available/IDES-Data-Preparation-Php-sample.conf ../sites-available/
RUN ln -s ../sites-available/IDES-Data-Preparation-Php-sample.conf

# php configs
# Edit 2016-09-06: This was for php5 ... now we're at php5, so commenting this out
# COPY etc/php5/php.ini /etc/php5/cli/php.ini
# COPY etc/php5/php.ini /etc/php5/apache2/php.ini

# Continue
COPY . /var/lib/IDES/
WORKDIR /var/lib/IDES/

# assert config availability
RUN test -f etc/config.yml && mkdir etc/ssl && mkdir -p cache/bkp && mkdir cache/downloads

RUN composer install --quiet

# copy test ssl files
RUN cp vendor/robrichards/xmlseclibs/tests/mycert.pem etc/ssl/ && \
    cp vendor/robrichards/xmlseclibs/tests/privkey.pem etc/ssl/ && \
    cp vendor/shadiakiki1986/fatca-ides-php/tests/FatcaIdesPhp/pubkey.pem etc/ssl/

# LAUNCH
ENTRYPOINT ["bash","entrypoint.sh"]
