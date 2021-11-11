FROM httpd:2.4

ADD . /tmp/code/

RUN apt-get update \
    # Install build dependencies
    && apt-get install -y npm nodejs-legacy git \
    # Install npm and bower packages required by build
    && npm install -g gulp bower \
    && cd /tmp/code \
    && npm install \
    && bower install --allow-root \
    # Build and deploy artificats into Apache webroot
    && gulp build \
    && cd /usr/local/apache2/htdocs \
    && tar xvf /tmp/code/artifacts/ogcpreview.tar.gz \
    && cp /tmp/code/docker/update-backend.sh /usr/local/bin/ \
    && chmod +x /usr/local/bin/update-backend.sh \
    # Configure GeoServer reverse proxy entry
    && cp /tmp/code/docker/geoserver.conf /usr/local/apache2/conf/extra/ \
    && echo "Include conf/extra/geoserver.conf" >> /usr/local/apache2/conf/httpd.conf \
    && echo "LoadModule proxy_module modules/mod_proxy.so" >> /usr/local/apache2/conf/httpd.conf \
    && echo "LoadModule proxy_http_module modules/mod_proxy_http.so" >> /usr/local/apache2/conf/httpd.conf \
    && rm -fr /tmp/code \
    # Purge all unneeded apt-get packages and caches
    && apt-get purge -y npm nodejs-legacy git \
    && apt-get -y autoremove \
    && apt-get -y clean \
    # Get rid of npm and bower cache directories
    && rm -fr /tmp/* \
    && rm -fr /usr/local/lib/node_modules \
    && rm -fr /root/.npm \
    && rm -fr /root/.cache \
    && cd

ENV GEOSERVER_HOSTNAME geoserver
ENV GEOSERVER_PORT 8080

EXPOSE 80
ENTRYPOINT ["/usr/local/bin/update-backend.sh"]
CMD ["httpd-foreground"]