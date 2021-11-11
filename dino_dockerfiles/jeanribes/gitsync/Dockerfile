FROM trafex/alpine-nginx-php7

COPY initrepo.sh /initrepo.sh
COPY app /var/www/html/git
RUN apk --update add git && chmod a+x /initrepo.sh;rm /var/www/html/index.php
CMD /initrepo.sh && /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
