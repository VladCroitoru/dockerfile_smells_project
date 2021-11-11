

FROM php:7.2.2-apache-stretch

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git nano wget python2.7 libfontconfig poppler-utils cron zlib1g-dev nano && \
    ln -s /usr/bin/pdftotext /usr/local/bin/pdftotext && \
    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
    tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
    mv phantomjs-2.1.1-linux-x86_64 /usr/local/share && \
    ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin

RUN git clone git://github.com/casperjs/casperjs.git /usr/local/casperjs && \
    cd /usr/local/casperjs && \
    ln -sf `pwd`/bin/casperjs /usr/local/bin/casperjs && \
    cd /usr/local/include && \
    ln -s /usr/bin/python2.7 /usr/bin/python




RUN git clone https://github.com/CLSPhila/casperscraping /usr/local/include/cpcmsNavigate && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli && docker-php-ext-install zip

ADD eg-cron /etc/cron.d/eg-cron

RUN chmod 0644 /etc/cron.d/eg-cron && \
    touch /var/log/cron.log && \
    cd /var/www && \
    rm -rf html && \
    git clone https://github.com/NateV/Expungement-Generator html && \
    cd html && \
    mkdir data && \
    mkdir docketsheets && \
    chown www-data:www-data data && \
    chown www-data:www-data docketsheets && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    composer install && \
    cp TemplateProcessor.php vendor/phpoffice/phpword/src/PhpWord/

COPY ./php.ini /usr/local/etc/php/php.ini
COPY ./docker-config.php /var/www/html/config.php

