# Image for running git projects in python
#
FROM alpine:3.8
LABEL authors="Marco Albero <periket2000@gmail.com>"

# openresty build
ENV OPENRESTY_VERSION=1.9.7.3 \
    PCRE_VERSION=8.37 \
    _prefix=/usr/local \
    _exec_prefix=/usr/local \
    _localstatedir=/var \
    _sysconfdir=/etc \
    _sbindir=/usr/local/sbin

# Installing lua resty-http
ENV LUA_RESTY_HTTP_VERSION 0.07 

# Installing lua-redis
ENV LUA_RESTY_REDIS_VERSION 0.03

# install dependencies
RUN apk update \
    && apk add gcc tar libtool zlib jemalloc jemalloc-dev perl \ 
    make musl-dev openssl-dev pcre-dev g++ zlib-dev curl python3 \
    perl-test-longstring perl-list-moreutils perl-http-message \
    geoip-dev sudo dnsmasq redis \
     && mkdir -p /tmp/nginx \
     && readonly NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
     && echo "using up to $NPROC threads" \
     && cd /tmp/nginx/ \
     && curl -k -L http://downloads.sourceforge.net/project/pcre/pcre/${PCRE_VERSION}/pcre-${PCRE_VERSION}.tar.gz -o /tmp/nginx/pcre-${PCRE_VERSION}.tar.gz \
     && curl -k -L https://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz -o /tmp/nginx/openresty-${OPENRESTY_VERSION}.tar.gz \
     && tar -zxf ./pcre-${PCRE_VERSION}.tar.gz \
     && tar -zxf ./openresty-${OPENRESTY_VERSION}.tar.gz \
     && cd /tmp/nginx/openresty-${OPENRESTY_VERSION} \
     && ./configure \
            --prefix=${_exec_prefix}/nginx \
            --sbin-path=${_sbindir}/nginx \
            --conf-path=${_sysconfdir}/nginx/api-gateway.conf \
            --error-log-path=${_localstatedir}/log/api-gateway/error.log \
            --http-log-path=${_localstatedir}/log/api-gateway/access.log \
            --pid-path=${_localstatedir}/run/api-gateway.pid \
            --lock-path=${_localstatedir}/run/api-gateway.lock \
            --with-pcre=../pcre-${PCRE_VERSION}/ --with-pcre-jit \
            --with-stream \
            --with-stream_ssl_module \
            --with-http_ssl_module \
            --with-http_stub_status_module \
            --with-http_realip_module \
            --with-http_addition_module \
            --with-http_sub_module \
            --with-http_dav_module \
            --with-http_geoip_module \
            --with-http_gunzip_module  \
            --with-http_gzip_static_module \
            --with-http_auth_request_module \
            --with-http_random_index_module \
            --with-http_secure_link_module \
            --with-http_degradation_module \
            --with-http_auth_request_module  \
            --with-http_v2_module \
            --with-luajit \
            --without-http_ssi_module \
            --without-http_userid_module \
            --without-http_uwsgi_module \
            --without-http_scgi_module \
            -j${NPROC} \
     && make -j${NPROC} \
     && make install \
     && echo " ... installing python and git ..." \
     && python3 -m ensurepip \
     && rm -r /usr/lib/python*/ensurepip \
     && pip3 install --upgrade pip setuptools \
     && pip3 install virtualenv \
     && apk --update add git build-base \
     && rm -r /root/.cache \
     && ln -s /usr/bin/python3 /usr/bin/python \
    && mkdir -p /tmp/nginx \
    && curl -k -L https://github.com/pintsized/lua-resty-http/archive/v${LUA_RESTY_HTTP_VERSION}.tar.gz -o /tmp/nginx/lua-resty-http-${LUA_RESTY_HTTP_VERSION}.tar.gz \
    && tar -xf /tmp/nginx/lua-resty-http-${LUA_RESTY_HTTP_VERSION}.tar.gz -C /tmp/nginx/ \
    && cd /tmp/nginx/lua-resty-http-${LUA_RESTY_HTTP_VERSION} \
    && make install \
    LUA_LIB_DIR=${_prefix}/nginx/lualib \
    && curl -k -L https://codeload.github.com/pintsized/lua-resty-redis-connector/tar.gz/v${LUA_RESTY_REDIS_VERSION} -o /tmp/nginx/lua-resty-redis-connector-${LUA_RESTY_REDIS_VERSION}.tar.gz \
    && tar -xf /tmp/nginx/lua-resty-redis-connector-${LUA_RESTY_REDIS_VERSION}.tar.gz -C /tmp/nginx/ \
    && cd /tmp/nginx/lua-resty-redis-connector-${LUA_RESTY_REDIS_VERSION} \
    && make install \
    LUA_LIB_DIR=${_prefix}/nginx/lualib \
    && rm -rf /tmp/nginx \
    && apk del gcc g++ build-base make \
    && rm -fr /usr/share /usr/libexec/gcc \
    && rm -fr /var/cache/apk \
    && find /usr/ -name '*pycache*' -exec rm -fr {} +;

ENV PROJECT_DIR /usr/local/pyenv
RUN mkdir -p /etc/periodic/1min
COPY scripts/refresh.sh /etc/periodic/1min/refresh
RUN mkdir -p ${PROJECT_DIR} \
    && mkdir -p /usr/local/var/www/htdocs/app \
    && chmod +x /etc/periodic/1min/refresh \
    && echo OK > /usr/local/var/www/htdocs/app/index.html

COPY init.sh ${PROJECT_DIR}/init-container.sh
COPY scripts/* ${PROJECT_DIR}/
COPY config/api-gateway.conf /etc/nginx
COPY config/mesos.conf /etc/nginx/conf.d/
COPY config/access.lua /etc/nginx/
COPY config/default.conf /etc/nginx/conf.d/
COPY certs/* /etc/nginx/

RUN adduser -S py-user -u 1000 \
    && addgroup -S py-user -g 1000 \
    && chown py-user:py-user ${PROJECT_DIR} \
    && chown py-user:py-user ${PROJECT_DIR}/*.sh \
    && chown py-user:py-user /usr/local/var/www/htdocs/app \
    && chown -R py-user:py-user /usr/lib/python* \
    && chown -R py-user:py-user /var/log/api-gateway \
    && chown -R py-user:py-user /etc/nginx \
    && chown -R py-user:py-user /usr/local/nginx \
    && chmod +x ${PROJECT_DIR}/*.sh \
    && echo "py-user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER py-user
ENTRYPOINT ${PROJECT_DIR}/init-container.sh
