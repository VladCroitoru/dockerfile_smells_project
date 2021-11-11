FROM klinche/php-fpm

LABEL maintainer "dbrooks@klinche.com"

RUN apt-get update && apt-get install -y supervisor python-setuptools python-pip

WORKDIR /var

RUN git clone https://github.com/peterfroehlich/supervisor-logging.git

WORKDIR /var/supervisor-logging
RUN pip install
RUN python setup.py install



WORKDIR /var/www/symfony

ENV SUPERVISOR_CONF ""
ENV WAIT_FOR_PHP "false"

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["supervisord", "-n","-c", "/etc/supervisor/conf.d/supervisord.conf", "-e", "debug"]

HEALTHCHECK CMD curl --fail "http://127.0.0.1:9001" || exit 1
