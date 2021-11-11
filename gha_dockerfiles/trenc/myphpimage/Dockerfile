FROM php:7.4-apache

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y -q --no-install-recommends default-mysql-client && \
    apt-get clean

RUN curl --location --output /usr/local/bin/mhsendmail https://github.com/mailhog/mhsendmail/releases/download/v0.2.0/mhsendmail_linux_amd64 && chmod +x /usr/local/bin/mhsendmail
RUN echo 'sendmail_path="/usr/local/bin/mhsendmail --smtp-addr=mailhog:1025 --from=no-root@localhost"' > /usr/local/etc/php/conf.d/mailhog.ini
RUN docker-php-ext-install mysqli
RUN a2enmod rewrite
