FROM alpine
RUN apk --no-cache --update \
    add nginx php5-fpm php5-cli php5-common \
    php5-suhosin php5-mysql php5-mysqli \
    php5-mcrypt php5-gd supervisor && \
    ln -s /dev/stdout /var/log/php-fpm.log && \
    ln -s /dev/stdout /var/log/supervisord.log && \
    ln -s /dev/stdout /var/log/nginx/access.log && \
    ln -s /dev/stdout /var/log/nginx/error.log && \
    sed -i 's/127\.0\.0\.1:9000/\/tmp\/php\.sock/' /etc/php5/php-fpm.conf && \
    sed -i 's/^include/;&/' /etc/php5/php-fpm.conf && \
    sed -i 's/;listen\.mode.*/listen.mode = 0666/g' /etc/php5/php-fpm.conf && \
    sed -i 's/^logfile/;&/' /etc/supervisord.conf && \
    rm /var/cache/apk/* && \
    mkdir -p /var/run/php-fpm && \
    mkdir /var/run/nginx && \
    rm -rf /var/www/localhost && \
    echo "<?php echo 'hello world<br />Server variables are:<br /><pre>'; print_r(\$_SERVER); echo '</pre>'?>" > /var/www/index.php

COPY  default.conf /etc/nginx/conf.d/default.conf
ADD   services.ini /etc/supervisor.d/services.ini
EXPOSE 80
CMD ["/usr/bin/supervisord"]
