FROM alpine:3.8

RUN apk --update add \
		openssl-dev \
		pcre-dev \
		zlib-dev \
		git \
		wget \
		build-base && \
		rm -rf /var/cache/apk/*

ENV nginx_home /var/tmp/nginx

ENV RUN_USER  proxy
ENV RUN_GROUP proxy

RUN adduser -u 1001 -S ${RUN_USER} && addgroup -S ${RUN_GROUP}
RUN mkdir -p ${nginx_home}

ENV nginx_version 1.9.7
ENV header_module_version 0.29

WORKDIR ${nginx_home}

RUN wget http://nginx.org/download/nginx-${nginx_version}.tar.gz \
    && git clone https://github.com/nginx-shib/nginx-http-shibboleth.git \
    && wget https://github.com/openresty/headers-more-nginx-module/archive/v${header_module_version}.tar.gz

RUN tar zxvf v${header_module_version}.tar.gz \
    && tar zxvf nginx-${nginx_version}.tar.gz \
    && cd ${nginx_home}/nginx-${nginx_version} \
    && ./configure --with-http_ssl_module \
                --with-pcre-jit \
                --with-http_auth_request_module \
                --add-module=${nginx_home}/nginx-http-shibboleth \
                --add-module=${nginx_home}/headers-more-nginx-module-${header_module_version} \
    && make \
    && make install

# Lets clean up
RUN rm -rf ${nginx_home} \
    && apk del git build-base

RUN mkdir -p /usr/local/nginx/ \
    && mkdir -p /usr/local/nginx/sites-enabled/ \
    && mkdir -p /usr/local/nginx/includes.d

ADD servers/sites-enabled /usr/local/nginx/sites-enabled/
ADD servers/conf /usr/local/nginx/conf/

RUN chmod -R 700 /usr/local/nginx/ \
    && chown -R ${RUN_USER}:${RUN_GROUP}  /usr/local/nginx/ \
    && rm -f /usr/local/nginx/conf/nginx.conf.default

EXPOSE 80 443

WORKDIR /usr/local/nginx

CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]
