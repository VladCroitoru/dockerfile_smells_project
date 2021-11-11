FROM debian:jessie

MAINTAINER "Juan Ramon Alfaro" <info@oondeo.es>

RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449
RUN echo deb http://dl.hhvm.com/debian jessie main | tee /etc/apt/sources.list.d/hhvm.list

RUN apt-get clean && \
    apt-get update && \
    apt-get install -y --no-install-recommends php-pear* php-mail php-mail-mime php-mail-mimedecode php-db php-http* php-auth* php-date php-mdb2 php-calendar php-soap php-xml* php-net-* php-html* php-text* php-file  wget && \
    apt-get install -y libgmp10 hhvm && \
    apt-get remove -y php-nette && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install php tools (composer / phpunit)
RUN cd /tmp && \
    wget https://getcomposer.org/composer.phar && \
    chmod +x composer.phar && \
    mv composer.phar /usr/local/bin/composer && \
    wget https://phar.phpunit.de/phpunit.phar && \
    chmod +x phpunit.phar && \
    mv phpunit.phar /usr/local/bin/phpunit

COPY php.ini /etc/hhvm/php.ini
COPY start.sh /start.sh

RUN mkdir -p /var/www /var/run/hhvm /var/lib/hhvm /var/log/hhvm && \
    chown -R www-data:www-data /var/www /var/run/hhvm /var/lib/hhvm /var/log/hhvm /etc/hhvm && \
    rm -f /etc/hhvm/server.ini


VOLUME [ "/var/www","/var/lib/hhvm/sessions" ]


USER www-data

ENV PORT=9000 DEVELOPMENT="false" COMPILE="true" ROOT="/var/www" COMPILE_OPTS="-l3 -v AllVolatile=true -v EnableEval=1"

EXPOSE 9000 8080 9001

CMD ["/start.sh"]

