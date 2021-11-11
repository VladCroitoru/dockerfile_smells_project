FROM php:5-fpm-alpine

ENV APP_BASE /var/www/html

# Install php extensions needed by simple-nuget-server
RUN docker-php-ext-install pdo_mysql && \
    docker-php-ext-enable pdo_mysql

# Configure php so it will daemonize instead of running in CLI mode (not needed, happens by default in php:5-fpm-alpine)
#RUN sed 's!daemonize = no!daemonize = yes!g' /usr/local/etc/php-fpm.d/docker.conf

# Copy in the project
COPY simple-nuget-server $APP_BASE
RUN rm -rf $APP_BASE/.git && \
    chown 0770 $APP_BASE/db $APP_BASE/packagefiles

# Add the entrypoint script which configures simple-nuget-server
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

# Configure simple-nuget-server
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["php-fpm"]