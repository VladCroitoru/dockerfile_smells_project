#
# Strass servi avec PHP-FCGI sur le port 8000.
#

FROM bersace/strass-sdk AS static

ADD Makefile .
ADD include/Strass ./include/Strass
ADD static/styles ./static/styles

RUN make clean all && \
    rm -rf static/styles/*/src && \
    :

FROM bersace/strass-runtime

ADD index.php .
ADD include ./include
ADD scripts/ ./scripts
COPY --from=static /strass/static ./static

VOLUME /strass/htdocs

ADD docker/php5-fpm.conf /etc/php5/fpm/php-fpm.conf
ADD docker/php5-fpm-pool.conf /etc/php5/fpm/pool.d/strass.conf
EXPOSE 8000

ADD docker/entrypoint.mk /usr/local/bin/entrypoint.mk
ENTRYPOINT ["/usr/local/sbin/tini", "-gw", "--", "/usr/local/bin/entrypoint.mk"]
CMD ["fcgi"]
