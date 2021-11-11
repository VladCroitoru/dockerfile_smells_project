FROM ridibooks/performance-apache-base:7.1
MAINTAINER Kang Ki Tae <kt.kang@ridi.com>

ENV APACHE_DOC_ROOT=/var/www/html/web
ENV APACHE_ALIAS=/super
ENV XDEBUG_ENABLE=0
ENV XDEBUG_HOST=""
ENV PHP_TIMEZONE=Asia/Seoul

ENV DEBUG=0
ENV SENTRY_KEY=""
ENV CMS_RPC_URL=http://localhost
ENV MYSQL_HOST=localhost
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=""
ENV MYSQL_DATABASE=cms

ADD ./docs/docker/cms-admin.conf /etc/apache2/sites-available/
ENTRYPOINT ["/var/www/html/docs/docker/docker-entrypoint.sh"]
CMD ["apache2-foreground"]

RUN a2enmod proxy proxy_http \
&& a2dissite 000-default \
&& a2ensite cms-admin

ADD . /var/www/html/
WORKDIR /var/www/html/
RUN make
