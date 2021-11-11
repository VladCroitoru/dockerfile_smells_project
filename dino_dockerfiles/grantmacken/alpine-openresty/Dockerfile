# syntax=docker/dockerfile:experimental
# Dockerfile grantmacken/alpine-openresty
# https://github.com/grantmacken/alpine-openresty
FROM docker.io/alpine:3.14.2 as bld
# LABEL maintainer="${GIT_USER_NAME} <${GIT_USER_EMAIL}>"

ARG PREFIX
ARG OPENRESTY_VER
ARG OPENSSL_PATCH_VER
ARG PCRE_VER
ARG ZLIB_VER
ARG OPENSSL_VER
ARG CMARK_VER

ARG ZLIB_PREFIX="${PREFIX}/zlib"
ARG ZLIB_LIB="$ZLIB_PREFIX/lib"
ARG ZLIB_INC="$ZLIB_PREFIX/include"

ARG PCRE_PREFIX="${PREFIX}/pcre"
ARG PCRE_LIB="${PCRE_PREFIX}/lib"
ARG PCRE_INC="${PCRE_PREFIX}/include"

ARG OPENSSL_PREFIX="${PREFIX}/openssl"
ARG OPENSSL_LIB="$OPENSSL_PREFIX/lib"
ARG OPENSSL_INC="$OPENSSL_PREFIX/include"

ARG CMARK_PREFIX="${PREFIX}/cmark"
ARG PATCHES_URL="https://raw.githubusercontent.com/openresty/openresty/master/patches"

# https://github.com/openresty/docker-openresty/blob/master/alpine/Dockerfile

RUN apk add --virtual .build-deps \
       build-base \
       gd-dev \
       linux-headers \
       openssl-dev \
       pcre-dev \
       perl-dev \
       zlib-dev \
    && apk add --update perl tzdata libgcc

WORKDIR = /home
ADD https://zlib.net/zlib-${ZLIB_VER}.tar.gz ./zlib.tar.gz
RUN echo ' - install zlib' \
    &&  tar -C /tmp -xf ./zlib.tar.gz \
    && cd /tmp/zlib-${ZLIB_VER} \
    && ./configure --prefix=${ZLIB_PREFIX} \
    && make \
    && make install \
    && rm -rf ${ZLIB_PREFIX}/share \
    && rm -rf ${ZLIB_PREFIX}/lib/pkgconfig \
    && rm -f /home/zlib.tar.gz \
    && rm -r /tmp/zlib-${ZLIB_VER} \
    && echo '---------------------------'

ADD https://ftp.pcre.org/pub/pcre/pcre-${PCRE_VER}.tar.gz ./pcre.tar.gz
RUN echo ' - install pcre' \
    &&  tar -C /tmp     -xf ./pcre.tar.gz \
    && cd /tmp/pcre-${PCRE_VER} \
    && ./configure \
    --disable-cpp \
    --prefix=${PCRE_PREFIX} \
    --enable-jit \
    --enable-utf \
    --enable-unicode-properties \
    && make \
    && make install \
    && rm -rf ${PCRE_PREFIX}/bin \
    && rm -rf ${PCRE_PREFIX}/share \
    && rm -f ${PCRE_PREFIX}/lib/*.la \
    && rm -f ${PCRE_PREFIX}/lib/*pcreposix* \
    && rm -rf ${PCRE_PREFIX}/lib/pkgconfig \
    && rm -f /home/pcre.tar.gz \
    && rm -r /tmp/pcre-${PCRE_VER} \
    && echo '---------------------------'

# https://github.com/openresty/openresty-packaging/blob/master/deb/openresty-openssl/debian/rules
ADD https://www.openssl.org/source/openssl-${OPENSSL_VER}.tar.gz ./openssl.tar.gz
RUN echo ' - install openssl' \
    && tar -C /tmp -xf ./openssl.tar.gz \
    && cd /tmp/openssl-${OPENSSL_VER} \
    && echo 'patching OpenSSL 1.1.1 for OpenResty' \
    && wget -qO- ${PATCHES_URL}/openssl-${OPENSSL_PATCH_VER}-sess_set_get_cb_yield.patch | patch -p1 --verbose \
   && ./config no-threads shared enable-ssl3 enable-ssl3-method \
    --prefix=${OPENSSL_PREFIX} \
    --libdir=lib \
    shared zlib \
    -I${ZLIB_INC} \
    -L${ZLIB_LIB} \
    -Wl,-rpath,${ZLIB_LIB}:${OPENSSL_LIB} \
    && make \
    && make install_sw \
    && rm -rf ${OPENSSL_PREFIX}/bin//bin/c_rehash \
    && rm -rf ${OPENSSL_PREFIX}/lib/pkgconfig \
    && rm -f /home/openssl.tar.gz \
    && rm -r /tmp/openssl-${OPENSSL_VER} \
    && echo '---------------------------'

ADD https://openresty.org/download/openresty-${OPENRESTY_VER}.tar.gz ./openresty.tar.gz
RUN echo    ' - install openresty' \
    && echo '   -----------------' \
    &&  tar -C /tmp -xf ./openresty.tar.gz \
    && mv /tmp/openresty-$OPENRESTY_VER /tmp/openresty \
    && cd /tmp/openresty \
    && ./configure \
    --prefix=${PREFIX} \
    --with-luajit-xcflags="-DLUAJIT_NUMMODE=2 -DLUAJIT_ENABLE_LUA52COMPAT" \
    --with-cc-opt="-DNGX_LUA_ABORT_AT_PANIC -I${OPENSSL_INC} -I${PCRE_INC} -I${ZLIB_INC}" \
    --with-ld-opt="-L${PCRE_LIB} -L${OPENSSL_LIB} -L${ZLIB_LIB} -Wl,-rpath,${PCRE_LIB}:${OPENSSL_LIB}:${ZLIB_LIB}" \
    --with-compat \
    --with-file-aio \
    --with-http_addition_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_realip_module \
    --with-http_secure_link_module \
    --with-http_slice_module \
    --with-http_ssl_module \
    --with-http_ssl_module \
    --with-http_v2_module \
    --with-ipv6 \
    --with-md5-asm \
    --with-pcre-jit \
    --with-sha1-asm \
    --with-stream \
    --with-stream_ssl_module \
    --with-stream_ssl_preread_module \
    --with-threads \
    --without-http_auth_basic_module \
    --without-http_empty_gif_module \
    --without-http_fastcgi_module \
    --without-http_memcached_module \
    --without-http_rds_csv_module \
    --without-http_rds_json_module \
    --without-http_redis_module \
    --without-http_redis2_module \
    --without-http_scgi_module \
    --without-http_ssi_module \
    --without-http_uwsgi_module \
    --without-lua_rds_parser \
    --without-mail_imap_module \
    --without-mail_pop3_module \
    --without-mail_smtp_module \
    && make \
    && make install \
    && rm -rf ${PREFIX}/luajit/share/man \
    && rm -rf ${PREFIX}/luajit/lib/libluajit-5.1.a \
    && rm -f /home/openresty.tar.gz \
    && rm -r /tmp/openresty \
    && rm -f ${PREFIX}/nginx/conf/win-utf ${PREFIX}/nginx/conf/koi-* \
    && echo '---------------------------'

# ADD https://github.com/commonmark/cmark/archive/${CMARK_VER}.tar.gz ./cmark.tar.gz
# RUN echo    ' - install cmark' \
#     && echo '   ---------------' \
#     && apk add --update cmake \
#     && tar -C /tmp -xf ./cmark.tar.gz \
#     && cd /tmp/cmark-${CMARK_VER} \
#     && cmake \
#     && make install \
#     && rm -f /home/cmark.tar.gz \
#     && rm -r /tmp/cmark-${CMARK_VER} \
#     && echo '---------------------------' 

RUN echo ' -  FINISH ' \
    && echo '   --------' \
    && echo ' -  remove apk install deps' \
    && apk del .build-deps \
    && echo '---------------------------'

##############################
# tag and keep this image to spin up
# - to use resty-cli
##############################


FROM docker.io/alpine:3.14.2 as resty
COPY --from=bld /usr/local /usr/local
RUN apk add --no-cache perl curl libgcc gd geoip libxslt \
    && echo ' - create special directories' \
    && mkdir -p /etc/letsencrypt \
    && mkdir -p /usr/local/openresty/nginx/html/.well-known/acme-challenge \
    && mkdir -p /usr/local/openresty/nginx/cache \
    && mkdir -p /usr/local/openresty/site/bin \
    && ln -s /usr/local/openresty/bin/* /usr/local/bin/ 
# && opm get cdbattags/lua-resty-jwt \
# && opm get bungle/lua-resty-reqargs \
# && opm get bungle/lua-resty-session \
# && opm get zmartzone/lua-resty-openidc

ENV LANG C.UTF-8
WORKDIR /usr/local/openresty
STOPSIGNAL SIGTERM
ENTRYPOINT ["resty" ]

##############################
# tag and keep this image to spin up
# - to add opm modules
##############################

FROM resty as opm
ENV LANG C.UTF-8
WORKDIR /usr/local/openresty
STOPSIGNAL SIGTERM
ENTRYPOINT ["opm"]

FROM docker.io/alpine:3.14.2 as proxy
COPY --from=resty /usr/local/openresty /usr/local/openresty
RUN apk add --no-cache libgcc gd geoip libxslt \
    && mkdir -p /etc/letsencrypt \
    && ln -s /usr/local/openresty/bin/* /usr/local/bin/

ENV OPENRESTY_HOME /usr/local/openresty
ENV LANG C.UTF-8
WORKDIR /usr/local/openresty
EXPOSE 80 443
STOPSIGNAL SIGTERM
ENTRYPOINT ["bin/openresty", "-g", "daemon off;"]
