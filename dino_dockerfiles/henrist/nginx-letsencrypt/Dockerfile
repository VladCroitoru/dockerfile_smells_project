FROM nginx:1.17-alpine

RUN mkdir -p /var/www/dehydrated \
    && mkdir -p /opt/dehydrated \
    && apk add -Uuv \
        # dehydrated uses bash
        bash \
        curl \
        openssl \
        supervisor \
    && curl -sfSL "https://github.com/lukas2511/dehydrated/archive/v0.6.5.tar.gz" \
       | tar zx -C /opt/dehydrated --strip 1 \
    \
    # provide backward compatibility with previous version
    && ln -s /var/www/dehydrated /var/www/letsencrypt

COPY nginx/* /etc/nginx/
COPY dehydrated/* /opt/dehydrated/
COPY container/* /

VOLUME ["/opt/dehydrated/certs", "/opt/dehydrated/accounts"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/supervisord", "-c", "/supervisord.conf"]
