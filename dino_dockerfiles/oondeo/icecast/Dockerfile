FROM oondeo/alpine
MAINTAINER info@oondeo.es

RUN addgroup -S icecast && \
    adduser -S icecast
    
RUN apk add --update \
        icecast \
        mailcap && \
        mkdir -p /etc/icecast && mv /etc/icecast.xml /etc/icecast/ && \
    rm -rf /var/cache/apk/*

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

CMD ["icecast", "-c", "/etc/icecast/icecast.xml"]
    
ENTRYPOINT ["/sbin/tini", "-g","--", "/entrypoint.sh"]    
