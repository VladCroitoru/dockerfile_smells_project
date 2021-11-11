FROM niiknow/openresty:0.2.0
LABEL maintainer="noogen <friends@niiknow.org>"
ENV AWS_DEFAULT_REGION="us-east-2" \
    LETSENCRYPT_URL="https://acme-staging.api.letsencrypt.org/directory" \
    HOME="/root" \
    USER="root"
USER root
WORKDIR /root
ARG LUA_RESTY_AUTO_SSL_VERSION="0.12.0"
ARG RESTY_OPENSSL_VERSION="1.0.2k"
RUN cd /tmp \
    printf "Build of moonship, date: %s\n"  `date -u +"%Y-%m-%dT%H:%M:%SZ"` >> /etc/BUILDS/zz-moonship && \
    apk add --no-cache \
      bash \
      coreutils \
      curl \
      diffutils \
      openssl \
      openssl-dev \
      grep \
      nano \
      less \
      python \
      py-pip \
      rsync \
      git \
      sed && \
    pip install --upgrade pip && \
    pip install awscli && \
    if [ -L /usr/bin/pkill ]; then rm /usr/bin/pkill; fi && \
    cd /tmp && \
    curl -fSL https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o openssl-${RESTY_OPENSSL_VERSION}.tar.gz && \
		tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz && \
    luarocks install lua-resty-http && \
    luarocks install lua-resty-auto-ssl $LUA_RESTY_AUTO_SSL_VERSION && \
    luarocks install moonscript && \
    luarocks install lua-lru && \
    luarocks install basexx  && \
    luarocks install lpath && \
    luarocks install lua-log && \
    luarocks install lua-cjson && \
    luarocks install luasocket && \
    luarocks install luasec && \
    luarocks install luaossl && \
    luarocks install --server=http://luarocks.org/dev ltn12 && \
    luarocks install mooncrafts && \
    addgroup -S nginx \
    && mkdir -p /var/cache/nginx \
    && adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \
    && mkdir -p /usr/local/openresty/nginx/conf/app/ssl \
    && openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 \
      -subj '/CN=sni-support-required-for-valid-ssl' \
      -keyout /usr/local/openresty/nginx/conf/app/ssl/resty-auto-ssl-fallback.key \
      -out /usr/local/openresty/nginx/conf/app/ssl/resty-auto-ssl-fallback.crt \
    && openssl dhparam -out /usr/local/openresty/nginx/conf/app/ssl/dhparam.pem 2048 \
    && chown -R nginx:nginx /usr/local/openresty/nginx/conf/app/ssl \
    && chown -R nginx:nginx /usr/local/openresty/nginx/logs/ \
    && ln -s /usr/local/openresty/nginx/logs/ /var/log/nginx \
    && apk --purge -v del py-pip \
    && mkdir -p /usr/local/openresty/nginx/conf/app/src/moonship \
    && rm -rf /var/cache/apk/* /tmp/*
COPY rootfs/. /
COPY lib/moonship/. /usr/local/openresty/nginx/conf/app/src/moonship/
RUN cd /tmp \
    && curl -fSL https://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz -o /tmp/GeoLiteCity.dat.gz \
    && gunzip -f GeoLiteCity.dat.gz \
    && rm -f /usr/local/openresty/nginx/conf/app/GeoLiteCity.dat \
    && mv GeoLiteCity.dat /usr/local/openresty/nginx/conf/app/GeoLiteCity.dat \
    && chown -R nginx:nginx /usr/local/openresty/nginx/conf/ \
    && mkdir -p /usr/local/openresty/nginx/conf-bak \
    && rsync --update -raz /usr/local/openresty/nginx/conf/* /usr/local/openresty/nginx/conf-bak \
    && rm -rf /var/cache/apk/* /tmp/*
EXPOSE 80 443
VOLUME ["/usr/local/openresty/nginx/conf"]
