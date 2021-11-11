FROM lsiobase/alpine:3.7

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL maintainer="dgreig"

ARG CADDY_ARCH="amd64"
ARG CADDY_PLUGS="http.ipfilter,http.login,http.jwt,tls.dns.cloudflare,http.reauth"

RUN \

 echo "**** install packages ****" && \
 apk add --no-cache \
	apache2-utils \
	git \
	libressl2.6-libssl \
	logrotate \
	nano \
	openssl \
    curl \
	libcap \
	inotify-tools \
	php7 \
	php7-fileinfo \
	php7-fpm \
	php7-json \
	php7-mbstring \
	php7-openssl \
	php7-session \
	php7-simplexml \
	php7-xml \
	php7-xmlwriter \
	php7-curl \
	php7-ldap \
	php7-pdo_sqlite \
	php7-sqlite3 \
	php7-session \
	php7-zip \
	php7-cgi \
	php7-zlib && \
 echo "**** install caddy and plugins ****" && \
 curl -o \
 /tmp/caddy.tar.gz -L \
	"https://caddyserver.com/download/linux/${CADDY_ARCH}?license=personal&plugins=${CADDY_PLUGS}" && \
 tar -xf \
 /tmp/caddy.tar.gz -C \
	/usr/local/bin/ && \
 echo "**** give caddy permissions to use low ports ****" && \
 setcap cap_net_bind_service=+ep /usr/local/bin/caddy

# copy local files
COPY root/ /

# set home for the user (acme needs this)
ENV HOME /config

# ports and volumes
EXPOSE 80 443
VOLUME /config
