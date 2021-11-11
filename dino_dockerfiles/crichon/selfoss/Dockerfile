from php:apache
maintainer Christophe Richon <moi@crichon.eu>
# thanks to Jens Erat <email@jenserat.de>

# Remove SUID programs
RUN for i in `find / -perm +6000 -type f`; do chmod a-s $i; done

# selfoss requirements: mod-headers, mod-rewrite, gd
RUN a2enmod headers rewrite && \
    apt-get update && \
    apt-get install -y unzip && \
    apt-get install -y libpng12-dev && \
    docker-php-ext-install gd

ADD https://github.com/SSilence/selfoss/releases/download/2.12/selfoss-2.12.zip /tmp/
RUN unzip /tmp/selfoss-*.zip -d /var/www/html && \
    rm /tmp/selfoss-*.zip /var/www/html/index.html && \
    ln -s /var/www/html/data/config.ini /var/www/html && \
    chown -R www-data:www-data /var/www/html

## create missing directories and fix files owner
#RUN mkdir -p /var/www/html/data/sqlite /var/www/html/data/cache /var/www/html/data/logs /var/www/html/data/thumbnails

# Extend maximum execution time, so /refresh does not time out
ADD https://raw.githubusercontent.com/php/php-src/master/php.ini-production /usr/local/etc/php/php.ini
RUN sed "s/default_socket_timeout = 60/default_socket_timeout = 600/" -i /usr/local/etc/php/php.ini

# Auto refresh each hour
RUN echo "#!/bin/bash \n while sleep 3600 \n do \n curl localhost/update \n done" \
    > update.sh && chmod +x update.sh
RUN echo "#!/bin/bash \n ./update.sh & \n apache2-foreground" \
    > launch.sh && chmod +x launch.sh

## override basic configuration (edit it to your likings)
#RUN sed s#base_url=#base_url=/# < defaults.ini | \
        #sed s#allow_public_update_access=#allow_public_update_access=1# | \
        #sed s#public=#public=1# > tmp && mv tmp data/config.ini \
        #&& rm defaults.ini

VOLUME /var/www/html/data
CMD ./launch.sh
