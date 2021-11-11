FROM ssweriduk/wordpress-alpine-nginx-scalable:latest
MAINTAINER Stephen Sweriduk <ssweriduk@gmail.com>

ENV \
    # Directory to store xdebug profiling
    XDEBUG_DIR="/tmp/xdebug" \
    # Use OSX IP address loopback hack: https://gist.githubusercontent.com/ralphschindler/535dc5916ccbd06f53c1b0ee5a868c93/raw/com.ralphschindler.docker_10254_alias.plist
    XDEBUG_REMOTE_HOST="10.254.254.254" \
    XDEBUG_REMOTE_PORT="9000" \
    # You can enable this env to allow profiling your application with xdebug trigger
    # This is disabled by default because it adds plenty of overhead when it's not needed
    # Default: disabled
    XDEBUG_ENABLE_PROFILE=1

#XDebug Dependencies
RUN apk update \
    && apk add --no-cache gcc autoconf g++ make rsync

RUN mv /usr/src/wordpress /usr/src/wordpress_bak \
    && mkdir /usr/src/wordpress \
    && chown www-data:www-data /usr/src/wordpress

#Expose wordpress source code for debugger to read
VOLUME /usr/src/wordpress

#Call all prior entrypoints
COPY entrypoint.sh /usr/local/bin/debug-entrypoint.sh
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh", "debug-entrypoint.sh" ]

#Override NGINX Https redirect
COPY vhost.conf /etc/nginx/conf.d/

#XDebug install & configure
RUN pecl channel-update pecl.php.net \
    && yes | pecl install xdebug-2.5.3 \
    && mkdir -p $XDEBUG_DIR

#Development configuration copy
COPY xdebug.ini /usr/local/etc/php/conf.d/
COPY php.ini /usr/local/etc/php/conf.d/

CMD [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf" ]
