FROM dabsquared/php-fpm

LABEL maintainer "dbrooks@dabsquared.com"

RUN apk add --no-cache supervisor py-setuptools py-pip procps

WORKDIR /var

RUN git clone https://github.com/peterfroehlich/supervisor-logging.git

WORKDIR /var/supervisor-logging
RUN pip install -r requirements.txt && python setup.py install

RUN rm /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

WORKDIR /var/www/symfony

ENV SUPERVISOR_CONF ""
ENV WAIT_FOR_PHP "false"

RUN mkdir -p /etc/supervisor/conf.d/

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["supervisord", "-n","-c", "/etc/supervisord.conf", "-e", "debug"]

HEALTHCHECK CMD curl --fail "http://127.0.0.1:9001" || exit 1
