FROM alpine:3.5

ENV HAPROXY_MAJOR=1.7 HAPROXY_VERSION=1.7.1 HAPROXY_MD5=d0acaae02e444039e11892ea31dde478

ENV ETCD_NODE="" CONFD_VERSION=0.11.0
ENV CONFD_PACKAGE="http://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64"

RUN set -x \
  && apk add --no-cache socat curl \
  && apk add --no-cache --virtual .build-deps \
       gcc \
       libc-dev \
       linux-headers \
       make \
       openssl-dev \
       pcre-dev \
       zlib-dev \
  && curl -SL "http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz" -o haproxy.tar.gz \
  && echo "${HAPROXY_MD5}  haproxy.tar.gz" | md5sum -c \
  && mkdir -p /usr/src \
  && tar -xzf haproxy.tar.gz -C /usr/src \
  && mv "/usr/src/haproxy-$HAPROXY_VERSION" /usr/src/haproxy \
  && rm haproxy.tar.gz \
  && make -C /usr/src/haproxy \
       TARGET=linux2628 \
       USE_PCRE=1 PCREDIR= \
       USE_OPENSSL=1 \
       USE_ZLIB=1 \
       all \
       install-bin \
  && mkdir -p /usr/local/etc/haproxy \
  && cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \
  && rm -rf /usr/src/haproxy \
  && runDeps="$( \
		scanelf --needed --nobanner --recursive /usr/local \
			| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
			| sort -u \
			| xargs -r apk info --installed \
			| sort -u \
	)" \
	&& apk add --virtual .haproxy-rundeps $runDeps \
	&& apk del .build-deps \
  && curl -SL $CONFD_PACKAGE -o /bin/confd \
  && chmod +x /bin/confd

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

VOLUME ["/etc/confd"]

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
