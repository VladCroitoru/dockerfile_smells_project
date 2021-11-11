ARG		HAPROXY_BRANCH=
ARG		HAPROXY_MAJOR=2.0
ARG		HAPROXY_VERSION=2.0.25
ARG		ALPINE_VERSION=3.12
ARG		CERTBOT_VERSION=1.8.0

FROM	python:alpine$ALPINE_VERSION AS build
ARG		HAPROXY_BRANCH
ARG		HAPROXY_MAJOR
ARG		HAPROXY_VERSION
ARG		CERTBOT_VERSION

RUN		{	apk --no-cache --update --virtual build-dependencies add \
				libc-dev \
				libffi-dev \
				openssl-dev \
				libxml2-dev \
				libxslt-dev \
				python2-dev \
				build-base \
				git \
				lua5.3-dev \
				zlib-dev \
				linux-headers \
				perl \
				pcre-dev \
				wget \
				tar ; \
		}

WORKDIR	/usr/src

RUN		{	wget -q https://www.haproxy.org/download/$HAPROXY_MAJOR/src/$HAPROXY_BRANCH/haproxy-$HAPROXY_VERSION.tar.gz ; \
			tar xzf haproxy-$HAPROXY_VERSION.tar.gz ; \
			git clone https://github.com/feurix/hatop.git ; \
		}

RUN		{	cd haproxy-$HAPROXY_VERSION \ 
				&& make all TARGET=linux-libc \  
					USE_LUA=1 LUA_INC=/usr/include/lua5.3 LUA_LIB=/usr/lib/lua5.3 \
					USE_OPENSSL=1 SSL_INC=/usr/include SSL_LIB=/usr/lib \
					USE_PCRE=1 PCREDIR= USE_ZLIB=1 \
				&& make install ; \    
		}

RUN		{	cp hatop/bin/hatop /usr/local/bin ; \
		}

RUN		{	apk del build-dependencies ; \
			rm -rf  /usr/local/share \
				/usr/local/lib/perl5 ; \
		}


FROM 		alpine:$ALPINE_VERSION
ARG		HAPROXY_VERSION
ARG 		BUILD_DATE
ARG 		VCS_REF
MAINTAINER	Joram Knaack <joramk@gmail.com>
LABEL 		org.label-schema.build-date=$BUILD_DATE \
    		org.label-schema.vcs-url="https://github.com/joramk/haproxy.git" \
    		org.label-schema.vcs-ref=$VCS_REF \
    		org.label-schema.schema-version="1.0.0-rc1" \
			org.label-schema.name="HAProxy $HAPROXY_VERSION" \
			org.label-schema.description="HAProxy $HAPROXY_VERSION with TLSv1.3" \
			org.label-schema.vendor="Joram Knaack" \
			org.label-schema.docker.cmd="docker run -d -p 80:80 -p 443:443 -v haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg joramk/haproxy"
ENV 		container docker

COPY --from=build	/usr/local 	/usr/local
COPY				assets		/usr/local

RUN		{	apk --no-cache --update add \
				openssl \ 
				libffi \
				python2 \
				lua5.3 \
				pcre \
				expat \
				incron \
				bash \
				zlib \
				certbot \
				socat \
				coreutils ; \
			apk update && apk upgrade ; \
			mkdir -p /usr/local/etc/haproxy/letsencrypt /usr/local/etc/letsencrypt ; \
			ln -s /usr/local/etc/haproxy /etc/haproxy ; \
			ln -s /usr/local/etc/letsencrypt /etc/letsencrypt ; \
			chmod +x /usr/local/sbin/* ; \
			rm -rf /var/cache/apk/* ; \
		}

EXPOSE			80 443
HEALTHCHECK CMD	kill -0 1 || exit 1
STOPSIGNAL		SIGUSR1
VOLUME			[ "/etc/haproxy", "/etc/letsencrypt" ]
ENTRYPOINT		[ "docker-entrypoint.sh" ]
CMD 			[ "haproxy", "-V", "-W", "-f", "/usr/local/etc/haproxy/haproxy.cfg" ]
