FROM alpine:3.4

MAINTAINER Vitaly Aminev <v@makeomatic.ru>

ENV CONSUL_TEMPLATE_VERSION=0.16.0 \
    HAPROXY_MAJOR=1.7 \
    HAPROXY_VERSION=1.7.1 \
    HAPROXY_MD5=d0acaae02e444039e11892ea31dde478 \
    LUAPATH=/usr/lib/lua5.3 \
    LUACPATH=/usr/lib/lua5.3 \
    INC_PATH="-I/usr/include/lua5.3"

# see http://sources.debian.net/src/haproxy/1.6.5-2/debian/rules/ for some helpful navigation of the possible "make" arguments
RUN set -x \
	&& apk add --no-cache --update --virtual .build-deps \
		curl \
    git \
		build-base \
		libc-dev \
		linux-headers \
		make \
		openssl-dev \
		pcre-dev \
		zlib-dev \
    wget \
    zip \
    lua5.3-dev \
  && git clone https://github.com/brunoos/luasec.git /lua-sec \
  && cd /lua-sec \
  && make linux \
  && make install \
  && cd / \
	&& curl -SL "http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz" -o haproxy.tar.gz \
	&& echo "${HAPROXY_MD5}  haproxy.tar.gz" | md5sum -c \
	&& mkdir -p /usr/src \
	&& tar -xzf haproxy.tar.gz -C /usr/src \
	&& mv "/usr/src/haproxy-$HAPROXY_VERSION" /usr/src/haproxy \
	&& make -C /usr/src/haproxy \
		TARGET=linux2628 \
		USE_PCRE=1 PCREDIR= \
		USE_OPENSSL=1 \
		USE_ZLIB=1 \
    USE_LUA=yes \
    LUA_LIB=${LUAPATH} \
    LUA_INC=/usr/include/lua5.3 LDFLAGS=-ldl \
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
  && wget https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \
  && unzip /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \
  && mv /consul-template /usr/local/bin/consul-template \
  && rm -rf \
    /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \
    /lua-sec \
    /*.tar.gz \
  && mkdir /haproxy \
	&& apk add --virtual .haproxy-rundeps $runDeps \
    bash \
    ca-certificates \
    git \
    inotify-tools \
	&& apk del .build-deps

# copy files over
COPY root /

VOLUME ["/consul-template", "/haproxy", "/etc/letsencrypt", "/var/acme-webroot"]
EXPOSE 80 443 8443
ENTRYPOINT ["/launch.sh"]
