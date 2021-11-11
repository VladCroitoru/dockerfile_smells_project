FROM giabar/gb-limesurvey-base:latest
LABEL maintainer="giabar@giabar.com"

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
COPY config.php /var/www/html/application/config/config.php
RUN ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh
COPY default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
ENV NEW_SERVER_NAME default
ENV ENABLE_SSL off

ENV DOWNLOAD_URL https://github.com/LimeSurvey/LimeSurvey/archive/3.15.4+181109.tar.gz
RUN set -x \
	&& curl -SL "$DOWNLOAD_URL" -o /tmp/lime.tar.gz \
    && tar xf /tmp/lime.tar.gz --strip-components=1 -C /var/www/html \
    && rm /tmp/lime.tar.gz \
    && chown -R www-data:www-data /var/www/html

EXPOSE 80 443
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["apache2-foreground"]
