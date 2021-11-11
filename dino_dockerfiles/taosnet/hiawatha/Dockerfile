FROM alpine:edge
MAINTAINER Chris Batis <clbatis@taosnet.com>

RUN apk --no-cache add musl libxslt zlib libxml2 mbedtls && \
	apk --no-cache add hiawatha --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted && \
	addgroup -S www-data && \
	adduser -S -G www-data -g "Web Server" -h "/var/www/hiawatha" web-srv

EXPOSE 80/tcp 443/tcp
ENTRYPOINT /usr/bin/hiawatha-wrapper
COPY app /
VOLUME ["/var/www", "/etc/hiawatha/sites.d", "/etc/hiawatha/tls"]
