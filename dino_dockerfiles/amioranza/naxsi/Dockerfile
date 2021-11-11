FROM alpine:latest

MAINTAINER Alexandre Mioranza <amioranza@mdcnet.ninja>

ENV NGINX_VERSION nginx-1.13.3
ENV NAXSI_VERSION 0.55.3
ENV GEOIP_VERSION 1.6.9
ENV MODSECURITY_VERSION 2.9.2
ENV LANG C.UTF-8
ENV LC_ALL=C
ENV WRKDIR /usr/src
ENV BUILD_PKGS="\
        apache2-dev \
        autoconf \
        automake \
        gd-dev \
        geoip-dev \
        libressl-dev \
        libtool \
        libxml2-dev \
        libxslt-dev \
        linux-headers \
        pcre-dev \
        perl-dev \
        python-dev \
        zlib-dev"

WORKDIR ${WRKDIR}

RUN apk --update add \
        apr-util \
        bash \
        build-base \
        ca-certificates \
        curl \
        git \
        libxml2 \
        m4 \
        openssl \
        pcre \
        python \
        py-pip \
        py-geoip \
        py2-geoip \
        unzip \
        zlib \
        ${BUILD_PKGS}

# Download all files extract and simplify directory names
RUN curl -LJO http://nginx.org/download/${NGINX_VERSION}.tar.gz \
    && tar -xvzf ${NGINX_VERSION}.tar.gz \
    && mv ${NGINX_VERSION} nginx \
    && curl -LJO https://github.com/nbs-system/naxsi/archive/${NAXSI_VERSION}.tar.gz \
    && tar -xzvf naxsi-${NAXSI_VERSION}.tar.gz \
    && mv naxsi-${NAXSI_VERSION} naxsi \
    && curl -LJO https://github.com/maxmind/geoip-api-c/releases/download/v${GEOIP_VERSION}/GeoIP-${GEOIP_VERSION}.tar.gz \
    && tar -zxvf GeoIP-${GEOIP_VERSION}.tar.gz \
    && curl -LJO http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz \
    && gunzip GeoIP.dat.gz \
    && mkdir -p /usr/local/share/GeoIP/ \
    && mv GeoIP.dat /usr/local/share/GeoIP/ \
    && curl -LJO https://www.modsecurity.org/tarball/${MODSECURITY_VERSION}/modsecurity-${MODSECURITY_VERSION}.tar.gz \
    && tar -xzvf modsecurity-${MODSECURITY_VERSION}.tar.gz \
    && mv modsecurity-${MODSECURITY_VERSION} modsecurity \
    && cd modsecurity \
    && curl -LJO https://raw.githubusercontent.com/SpiderLabs/ModSecurity/master/modsecurity.conf-recommended \
    && curl -LJO https://raw.githubusercontent.com/SpiderLabs/ModSecurity/v2/master/unicode.mapping \
    && cd ${WRKDIR}


COPY naxsi/nxapi /opt/nxapi

RUN echo "" \
    && echo "" \
    && echo "##################  NXAPI INSTALL ##################" \
    && echo "" \
    && echo "" \
    && sleep 1 \
    && cd /opt/nxapi \
    && pip install -r requirements.txt \
    && python setup.py install \
    && echo "" \
    && echo "" \
    && echo "##################  GEOIP INSTALL ##################" \
    && echo "" \
    && echo "" \
    && sleep 1 \
    && cd ${WRKDIR}/GeoIP-${GEOIP_VERSION} \
    && ./configure \
    && make \
    && make check \
    && make install \
    && pip install GeoIP \
    && echo "" \
    && echo "" \
    && echo "##################  MODSECURITY INSTALL ##################" \
    && echo "" \
    && echo "" \
    && sleep 1 \
    && cd ${WRKDIR}/modsecurity \
    && ./autogen.sh \
    && ./configure --enable-standalone-module --disable-mlogc \
    && make \
    && make install \
    && echo "" \
    && echo "" \
    && echo "##################  NGINX INSTALL ##################" \
    && echo "" \
    && echo "" \
    && sleep 1 \
    && addgroup -S nginx \
    && adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \
    && cd ${WRKDIR}/nginx \
    && ./configure \
    --add-module=../naxsi/naxsi_src/ \
    --add-module=${WRKDIR}/modsecurity/nginx/modsecurity \
    --prefix=/etc/nginx \
    --sbin-path=/usr/local/sbin/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --pid-path=/run/nginx.pid \
    --lock-path=/run/nginx.lock \
    --http-log-path=/var/log/nginx/access.log \
    --error-log-path=/var/log/nginx/error.log \
    --http-client-body-temp-path=/var/cache/nginx/client_temp \
    --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
    --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
    --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
    --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
    --user=nginx \
    --group=nginx \
    --with-http_ssl_module \
    --with-http_realip_module \
    --with-http_addition_module \
    --with-http_sub_module \
    --with-http_dav_module \
    --with-http_flv_module \
    --with-http_mp4_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_random_index_module \
    --with-http_secure_link_module \
    --with-http_stub_status_module \
    --with-http_auth_request_module \
    --with-http_xslt_module=dynamic \
    --with-http_image_filter_module=dynamic \
    --with-http_geoip_module \
    --with-http_perl_module=dynamic \
    --with-threads \
    --with-stream \
    --with-stream_ssl_module \
    --with-http_slice_module \
    --with-mail \
    --with-mail_ssl_module \
    --with-file-aio \
    --with-http_v2_module \
    --with-ipv6 \
    && make \
    && make install \
    && echo "" \
    && echo "" \
    && echo "##################  CLEANUP BUILD PKGS AND SOURCES ##################" \
    && echo "" \
    && echo "" \
    && sleep 1 \
    && apk del ${BUILD_PKGS} \
    && rm /usr/local/lib/libGeoIP.a \
    && rm -rf /var/cache/apk/* \
    && echo "" \
    && echo "" \
    && echo "##################  MISC TASKS ##################" \
    && echo "" \
    && echo "" \
    && sleep 1 \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && mkdir -p /etc/naxsi \
    && cp /usr/src/naxsi/naxsi_config/naxsi_core.rules /etc/naxsi \
    && mkfifo /var/log/nginx/error_pipe.log \
    && cat ${WRKDIR}/modsecurity/modsecurity.conf-recommended  > /etc/nginx/modsecurity.conf \
    && cp ${WRKDIR}/modsecurity/unicode.mapping /etc/nginx/ \
    && cd /etc/nginx \
    && git clone https://github.com/SpiderLabs/owasp-modsecurity-crs \
    && mv owasp-modsecurity-crs/crs-setup.conf.example owasp-modsecurity-crs/crs-setup.conf \
    && mv owasp-modsecurity-crs/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example \
          owasp-modsecurity-crs/rules/REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf \
    && mv owasp-modsecurity-crs/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example \
          owasp-modsecurity-crs/rules/RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf \
    && echo "" \
    && echo "" \
    && echo "##################  COPYING FILES / TEMPLATES ##################" \
    && echo "" \
    && echo ""

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/sites-enabled/default /etc/nginx/sites-enabled/default
COPY nginx/modsec_includes.conf /etc/nginx/modsec_includes.conf
COPY default.html /var/www/html/index.html
COPY 50x.html /var/www/html/50x.html
COPY ssl-cert.pem /etc/nginx/ssl/ssl-cert.pem
COPY ssl-key.pem /etc/nginx/ssl/ssl-key.pem
COPY naxsi_whitelist.rules /etc/naxsi/naxsi_whitelist.rules
COPY es-index.json ${WRKDIR}
COPY naxsi_startup.sh /

RUN chmod +x /naxsi_startup.sh

EXPOSE 80 443

WORKDIR /

CMD ["/naxsi_startup.sh", "elasticsearch"]
