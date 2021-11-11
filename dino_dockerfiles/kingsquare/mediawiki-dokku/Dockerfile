FROM kingsquare/mediawiki:1.31.1

# install redis php module
# update upstream composer
RUN pecl install redis && docker-php-ext-enable redis && composer self-update && composer clearcache

# add dokku configuration
COPY conf /conf

# override entrypoint
COPY bin/dokku-entrypoint.sh /dokku-entrypoint.sh
ENTRYPOINT ["/dokku-entrypoint.sh"]
CMD ["apachectl", "-e", "info", "-D", "FOREGROUND"]
