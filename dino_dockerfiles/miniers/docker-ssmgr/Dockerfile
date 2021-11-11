FROM mhart/alpine-node:8

MAINTAINER miniers <m@lk.mk>

ENV SSMGR_TYPE client
ENV S6_OVERLAY_VERSION v1.21.7.0
ENV SS_VER 3.2.1
ENV SS_URL https://github.com/shadowsocks/shadowsocks-libev/archive/v$SS_VER.tar.gz
ENV SS_DIR shadowsocks-libev-$SS_VER

ENV REDIS_VERSION 5.0.3
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-5.0.3.tar.gz
ENV REDIS_DOWNLOAD_SHA e290b4ddf817b26254a74d5d564095b11f9cd20d8f165459efa53eb63cd93e02

RUN addgroup -S redis && adduser -S -G redis redis

RUN set -ex; \
	\
	apk add --no-cache --virtual .build-deps \
		coreutils \
		gcc \
		jemalloc-dev \
		linux-headers \
		make \
		musl-dev \
	; \
	\
	wget -O redis.tar.gz "$REDIS_DOWNLOAD_URL"; \
	echo "$REDIS_DOWNLOAD_SHA *redis.tar.gz" | sha256sum -c -; \
	mkdir -p /usr/src/redis; \
	tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1; \
	rm redis.tar.gz; \
	\
# disable Redis protected mode [1] as it is unnecessary in context of Docker
# (ports are not automatically exposed when running inside Docker, but rather explicitly by specifying -p / -P)
# [1]: https://github.com/antirez/redis/commit/edd4d555df57dc84265fdfb4ef59a4678832f6da
	grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 1$' /usr/src/redis/src/server.h; \
	sed -ri 's!^(#define CONFIG_DEFAULT_PROTECTED_MODE) 1$!\1 0!' /usr/src/redis/src/server.h; \
	grep -q '^#define CONFIG_DEFAULT_PROTECTED_MODE 0$' /usr/src/redis/src/server.h; \
# for future reference, we modify this directly in the source instead of just supplying a default configuration flag because apparently "if you specify any argument to redis-server, [it assumes] you are going to specify everything"
# see also https://github.com/docker-library/redis/issues/4#issuecomment-50780840
# (more exactly, this makes sure the default behavior of "save on SIGTERM" stays functional by default)
	\
	make -C /usr/src/redis -j "$(nproc)"; \
	make -C /usr/src/redis install; \
	\
	rm -r /usr/src/redis; \
	\
	runDeps="$( \
		scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \
			| tr ',' '\n' \
			| sort -u \
			| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
	)"; \
	apk add --virtual .redis-rundeps $runDeps; \
	apk del .build-deps; \
	\
	redis-server --version

RUN mkdir /data && chown redis:redis /data

RUN apk add --update --no-cache curl tzdata && \
    curl -sSL https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
    | tar xfz - -C / && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del curl && \
    rm -rf /var/cache/apk/*
    
RUN set -ex \
    && apk add --no-cache libcrypto1.0 \
                          libev \
                          libsodium \
                          mbedtls \
                          c-ares \
                          pcre \
    && apk add --no-cache --virtual .build-deps \
        autoconf \
        automake \
        asciidoc \
        xmlto \
        gettext-dev \
        build-base \
        curl \
        libev-dev \
        unzip \
        c-ares-dev \
        libtool \
        linux-headers \
        openssl-dev \
        libsodium-dev \
        mbedtls-dev \
        pcre-dev \
        tar \
        wget \
        git \
    && curl -ksSL $SS_URL | tar xz \
    && cd $SS_DIR \
        && curl -ksSL https://github.com/shadowsocks/ipset/archive/shadowsocks.tar.gz | tar xz --strip 1 -C libipset \
        && curl -ksSL https://github.com/shadowsocks/libcork/archive/shadowsocks.tar.gz | tar xz --strip 1 -C libcork \
        && curl -ksSL https://github.com/shadowsocks/libbloom/archive/master.tar.gz | tar xz --strip 1 -C libbloom \
        && ./autogen.sh \
        && ./configure --disable-documentation \
        && make install \
        && cd .. \
    && git config --global http.sslVerify false \
    && git clone https://github.com/shadowsocks/simple-obfs \
    && cd simple-obfs \
    && git submodule update --init --recursive \
    && ./autogen.sh \
    && ./configure \
    && make \
    && make install \
    && cd .. \
    && rm -rf simple-obfs \
    && apk del .build-deps \
    && rm -rf client_linux_amd64 \
        $SS_DIR \
        simple-obfs-$SIMPLE_OBFS_VERSION \
        /var/cache/apk/*

RUN apk add --no-cache  git \ 
    && git clone https://github.com/shadowsocks/shadowsocks-manager.git /ssmgr \
    && cd /ssmgr \
    && yarn

ADD root /

EXPOSE 4001 80 6379 38000-38100

ENTRYPOINT ["/init"]