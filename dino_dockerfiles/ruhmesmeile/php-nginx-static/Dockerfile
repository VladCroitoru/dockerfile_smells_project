FROM ruhmesmeile/php-nginx-typo3:7.2

# Change the following PHP settings for static pages (less RAM, smaller and static FPM pool)
# Configure PHP
COPY config/php/99-docker.php.ini /usr/local/etc/php/conf.d/99-docker.ini

# Configure PHP FPM
COPY config/php/application.conf /usr/local/etc/php-fpm.d/application.conf

# Configure Nginx (remove changelog.* from deny all)
RUN rm -f /opt/docker/etc/nginx/vhost.common.d/05-security.conf
COPY config/nginx/vhost.common.d/05-security.conf /opt/docker/etc/nginx/vhost.common.d/05-security.conf

# If this images uses a local API, expose it on port 3003
EXPOSE 3003
