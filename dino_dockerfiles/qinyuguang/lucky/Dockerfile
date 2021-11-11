FROM qinyuguang/yafbase:latest

VOLUME ["/home/logs/project/lucky", "/home/logs/php/lucky", "/var/mail"]

COPY ./ /www/lucky/
COPY ./src/conf/crontab /etc/cron.d/lucky
COPY ./conf/online/php.ini /usr/local/etc/php/php.ini
COPY ./conf/online/fpm.conf /usr/local/etc/php-fpm.d/lucky.conf

WORKDIR /www/lucky

RUN chmod 0644 /etc/cron.d/lucky \
    && crontab /etc/cron.d/lucky

CMD ["cron", "-f"]

