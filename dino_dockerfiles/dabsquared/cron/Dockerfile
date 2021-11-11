FROM dabsquared/php-fpm

LABEL maintainer "dbrooks@dabsquared.com"

WORKDIR /var/www/symfony

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

RUN rm /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD tail -f /var/log/cron.log
