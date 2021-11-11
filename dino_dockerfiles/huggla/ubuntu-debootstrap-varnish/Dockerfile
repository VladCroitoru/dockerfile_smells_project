FROM blitznote/debootstrap-amd64:18.04

COPY ./bin/entry.sh /usr/local/bin/entry.sh
COPY ./varnish-5.0-configuration-templates/default.vcl "/varnishconf/default.vcl"

RUN curl -s https://packagecloud.io/install/repositories/varnishcache/varnish5/script.deb.sh | bash \
 && apt-get install -qy varnish \
 && rm -rf /var/lib/apt/lists/* \
 && cp /etc/default/varnish /varnishconf/varnish \
 && chmod ugo+x /usr/local/bin/entry.sh

WORKDIR /varnishconf

VOLUME /varnishconf

EXPOSE 80 6082

CMD ["entry.sh"]
