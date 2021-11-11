FROM ioos/catalog-docker-base

COPY ./contrib/my_init.d /etc/my_init.d

RUN echo "Listen 8080" > /etc/apache2/ports.conf

COPY ./contrib/config/pycsw-apache.conf /etc/apache2/sites-available/pycsw_default.conf

RUN a2ensite pycsw_default
RUN a2dissite 000-default
RUN a2dissite ckan_default

CMD ["/sbin/my_init", "--", "/bin/services/pycsw/run"]


