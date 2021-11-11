FROM openresty/openresty:bionic

ENV DIFFIE_HELLMAN='' ALLOWED_DOMAINS='.*' AUTO_SSL_VERSION='0.13.1' FORCE_HTTPS='true' SITES='' LETSENCRYPT_URL='https://acme-v02.api.letsencrypt.org/directory'

RUN apt-get update \
 && apt-get install -y libpcre3 libpcre3-dev \
 && /usr/local/openresty/luajit/bin/luarocks install lua-resty-auto-ssl $AUTO_SSL_VERSION \
 && /usr/local/openresty/luajit/bin/luarocks install lrexlib-PCRE \
 && curl -L https://raw.githubusercontent.com/yourpalmark/mobile-detect.lua/master/mobile-detect.lua -o /usr/local/openresty/lualib/mobile-detect.lua \
 && openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 -subj '/CN=sni-support-required-for-valid-ssl' -keyout /etc/ssl/resty-auto-ssl-fallback.key -out /etc/ssl/resty-auto-ssl-fallback.crt

COPY nginx-cache-purge /nginx-cache-purge
COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf
