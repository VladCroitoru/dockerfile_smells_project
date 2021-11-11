FROM alpine:latest
LABEL maintainer "morten@abildgaard.org"

ENV DOKUWIKI_VERSION release_stable_2017-02-19b

RUN apk upgrade --no-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/

RUN apk --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ add \
    libwebp

RUN apk --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ add \
    php7 php7-fpm php7-gd php7-session php7-xml nginx supervisor git

RUN set -xe && \
    mkdir -p /run/nginx && \
    mkdir -p /var/www /var/dokuwiki-storage/data && \
    cd /var/www && \
    git init && \
    git remote add origin https://github.com/splitbrain/dokuwiki.git && \
    git fetch origin && \
    git checkout $DOKUWIKI_VERSION
# && \
#    mv /var/www/data/pages /var/dokuwiki-storage/data/pages && \
#    ln -s /var/dokuwiki-storage/data/pages /var/www/data/pages && \
#    mv /var/www/data/meta /var/dokuwiki-storage/data/meta && \
#    ln -s /var/dokuwiki-storage/data/meta /var/www/data/meta && \
#    mv /var/www/data/media /var/dokuwiki-storage/data/media && \
#    ln -s /var/dokuwiki-storage/data/media /var/www/data/media && \
#    mv /var/www/data/media_attic /var/dokuwiki-storage/data/media_attic && \
#    ln -s /var/dokuwiki-storage/data/media_attic /var/www/data/media_attic && \
#    mv /var/www/data/media_meta /var/dokuwiki-storage/data/media_meta && \
#    ln -s /var/dokuwiki-storage/data/media_meta /var/www/data/media_meta && \
#    mv /var/www/data/attic /var/dokuwiki-storage/data/attic && \
#    ln -s /var/dokuwiki-storage/data/attic /var/www/data/attic && \
#    mv /var/www/conf /var/dokuwiki-storage/conf && \
#    ln -s /var/dokuwiki-storage/conf /var/www/conf

ADD nginx.conf /etc/nginx/nginx.conf
ADD supervisord.conf /etc/supervisord.conf
ADD start.sh /start.sh

RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php7/php-fpm.ini && \
    sed -i -e "s|;daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf && \
    sed -i -e "s|listen\s*=\s*127\.0\.0\.1:9000|listen = /var/run/php-fpm7.sock|g" /etc/php7/php-fpm.d/www.conf && \
    sed -i -e "s|;listen\.owner\s*=\s*|listen.owner = |g" /etc/php7/php-fpm.d/www.conf && \
    sed -i -e "s|;listen\.group\s*=\s*|listen.group = |g" /etc/php7/php-fpm.d/www.conf && \
    sed -i -e "s|;listen\.mode\s*=\s*|listen.mode = |g" /etc/php7/php-fpm.d/www.conf && \
    chmod +x /start.sh

EXPOSE 80
VOLUME ["/var/www/data"]

ENTRYPOINT ["/start.sh"]
