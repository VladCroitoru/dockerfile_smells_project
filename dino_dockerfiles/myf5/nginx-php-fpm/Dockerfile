FROM php:7.4.6-fpm-alpine

MAINTAINER Jing Lin <web@myf5.net>

ENV NGINX_VERSION 1.12.1
ENV OPENSSL_VERSION 1.0.2l
ENV OPENSSL_CHACHA https://raw.githubusercontent.com/cloudflare/sslconfig/master/patches/openssl__chacha20_poly1305_draft_and_rfc_ossl102j.patch
ENV NGX_VERSION_TRANSPARENCY=1.3.2
ENV NGX_VERSION_BROTLI=1.0.2

ENV php_conf /usr/local/etc/php-fpm.conf
ENV fpm_conf /usr/local/etc/php-fpm.d/www.conf
ENV php_vars /usr/local/etc/php/conf.d/docker-vars.ini

###################################
# OPENSSL                         #
###################################

RUN	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		make \
		pcre-dev \
		zlib-dev \
		linux-headers \
		curl \
		gnupg \
		libxslt-dev \
		gd-dev \
		geoip-dev \
		perl-dev \
		wget \
		ca-certificates \
		g++ \
		zip \
	&& mkdir -p /usr/src \
	&& wget https://openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz \
	&& tar zxvf openssl-$OPENSSL_VERSION.tar.gz -C /usr/src \
	&& rm openssl-$OPENSSL_VERSION.tar.gz \
	&& wget -O /usr/src/chacha.patch $OPENSSL_CHACHA \
	&& cd /usr/src/openssl-$OPENSSL_VERSION \
	&& patch -p1 < ../chacha.patch \
	&& ./config \
	&& make depend
	
###################################
# CERTIFICATE TRANSPARENCY        #
###################################

COPY nginx-ct-1.3.2.zip /tmp/
RUN unzip /tmp/nginx-ct-1.3.2.zip -d /usr/src \
	&& rm /tmp/nginx-ct-1.3.2.zip \
	&& echo "CT copyed and unzipped"

###################################
# GOOGLE BROTLI      			  #
###################################

COPY ngx_brotli-1.0.2.zip /tmp/
RUN unzip /tmp/ngx_brotli-1.0.2.zip -d /usr/src \
	&& rm /tmp/ngx_brotli-1.0.2.zip \
	&& echo "BROTILI copyed and unzipped"

###################################
# TLS Dynamic Reord Sizing		  #
# Patch for NGINX      			  #
###################################

RUN wget -O /usr/src/nginx-dynamic_tls.patch https://raw.githubusercontent.com/cloudflare/sslconfig/master/patches/nginx__1.11.5_dynamic_tls_records.patch \
	&& echo "TLS Dynamic Reord Sizing patch downloaded"



###################################
# NGINX                           #
###################################
		
ENV GPG_KEYS B0F4253373F8F6F510D42178520A9993A1C052F8
ENV CONFIG "\
	--prefix=/usr/local/nginx \
	--sbin-path=/usr/sbin/nginx \
	--modules-path=/usr/lib/nginx/modules \
	--conf-path=/usr/local/nginx/conf/nginx.conf \
	--error-log-path=/var/log/nginx/error.log \
	--http-log-path=/var/log/nginx/access.log \
	--pid-path=/var/run/nginx.pid \
	--lock-path=/var/run/nginx.lock \
	--http-client-body-temp-path=/var/cache/nginx/client_temp \
	--http-proxy-temp-path=/var/cache/nginx/proxy_temp \
	--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
	--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
	--http-scgi-temp-path=/var/cache/nginx/scgi_temp \
	--user=www \
	--group=www \
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
	--with-http_geoip_module=dynamic \
	--with-http_perl_module=dynamic \
	--with-threads \
	--with-stream \
	--with-stream_ssl_module \
	--with-http_slice_module \
	--with-mail \
	--with-mail_ssl_module \
	--with-stream_ssl_preread_module \
    --with-stream_realip_module \
    --with-stream_geoip_module=dynamic \
	--with-file-aio \
	--with-http_v2_module \
	--with-compat \
	--with-openssl=/usr/src/openssl-$OPENSSL_VERSION \
	--add-module=/usr/src/nginx-ct-${NGX_VERSION_TRANSPARENCY} \
	--add-module=/usr/src/ngx_brotli-${NGX_VERSION_BROTLI} \
	"

RUN \
	addgroup -S www \
	&& adduser -D -S -h /var/cache/www -s /sbin/nologin -G www www \
	&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o nginx.tar.gz \
	&& tar -zxC /usr/src -f nginx.tar.gz \
	&& rm nginx.tar.gz \
	&& cd /usr/src/nginx-$NGINX_VERSION \
	&& patch -p1 < /usr/src/nginx-dynamic_tls.patch \
	&& echo "Dynamic TLS size recording pathed for nginx" \
	&& ./configure $CONFIG --with-debug \
    && sed -i "s/-Werror//g" /usr/src/nginx-$NGINX_VERSION/objs/Makefile \
	&& make \
	&& mv objs/nginx objs/nginx-debug \
	&& mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-debug.so \
	&& mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-debug.so \
	&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \
	&& mv objs/ngx_http_perl_module.so objs/ngx_http_perl_module-debug.so \
	&& ./configure $CONFIG \
    && sed -i "s/-Werror//g" /usr/src/nginx-$NGINX_VERSION/objs/Makefile \
	&& make \
	&& make install \
	&& rm -rf /usr/local/nginx/html/ \
	&& mkdir /usr/local/nginx/vhost/ \
	&& mkdir /usr/local/nginx/ssl/ \
	&& mkdir -p /var/cache/nginx/client_temp \
	&& mkdir -p /var/cache/nginx/proxy_temp \
	&& mkdir -p /var/cache/nginx/fastcgi_temp \
	&& mkdir -p /var/cache/nginx/uwsgi_temp \
	&& mkdir -p /var/cache/nginx/scgi_temp \
	&& mkdir -p /home/wwwlogs/ \
	&& mkdir -p /home/wwwroot/myf5/ \
	&& mkdir -p /etc/letsencrypt/sct/ \
	&& install -m644 html/index.html /home/wwwroot/myf5/ \
	&& install -m644 html/50x.html /home/wwwroot/myf5/ \
	&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \
	&& install -m755 objs/ngx_http_xslt_filter_module-debug.so /usr/lib/nginx/modules/ngx_http_xslt_filter_module-debug.so \
	&& install -m755 objs/ngx_http_image_filter_module-debug.so /usr/lib/nginx/modules/ngx_http_image_filter_module-debug.so \
	&& install -m755 objs/ngx_http_geoip_module-debug.so /usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \
	&& install -m755 objs/ngx_http_perl_module-debug.so /usr/lib/nginx/modules/ngx_http_perl_module-debug.so \
	&& ln -s ../../usr/lib/nginx/modules /usr/local/nginx/modules \
	&& strip /usr/sbin/nginx* \
	&& strip /usr/lib/nginx/modules/*.so \
	&& runDeps="$( \
		scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so \
			| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
			| sort -u \
			| xargs -r apk info --installed \
			| sort -u \
	)" \
	&& apk add --virtual .nginx-rundeps $runDeps \
	&& apk del .build-deps \
	&& rm -rf /usr/src/openssl-$OPENSSL_VERSION \
	&& rm -rf /usr/src/nginx-ct-$GX_VERSION_TRANSPARENCY \
	&& rm -rf /usr/src/ngx_brotli-$NGX_VERSION_BROTLI \
	&& rm -rf /usr/src/nginx-dynamic_tls.patch \
	&& rm -rf /usr/src/nginx-$NGINX_VERSION \
	&& apk add --no-cache gettext \
	\
	# forward request and error logs to docker log collector
	&& ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log \

# COPY pre defined file, make sure there is correct nginx configuration files, these files are based my own nginx.
COPY nginx.conf /usr/local/nginx/conf/nginx.conf
COPY enable-php.conf /usr/local/nginx/conf/enable-php.conf
COPY fastcgi.conf /usr/local/nginx/conf/fastcgi.conf
COPY wordpress.conf /usr/local/nginx/conf/wordpress.conf
COPY ./vhost/nginx.vh.default.conf /usr/local/nginx/conf/vhost/default.conf
COPY ./ssl/* /usr/local/nginx/conf/ssl/
COPY digicert.sct /etc/letsencrypt/sct/digicert.sct
COPY icarus.sct /etc/letsencrypt/sct/icarus.sct
COPY Shanghai /etc/localtime 



########Start PHP##########
RUN echo @testing 	>> /etc/apk/repositories && \
    echo /etc/apk/respositories && \
    apk update && \
    apk add --no-cache bash \
    openssh-client \
    wget \
    supervisor \
    curl \
    libcurl \
    git \
    python \
    python-dev \
    py-pip \
    augeas-dev \
    openssl-dev \
    ca-certificates \
    dialog \
    gcc \
    musl-dev \
    linux-headers \
    libmcrypt-dev \
    libpng-dev \
    icu-dev \
    libpq \
    libzip \
    libzip-dev \
    libxslt-dev \
    libffi-dev \
    libmemcached-dev \
    cyrus-sasl-dev \
    freetype-dev \
    sqlite-dev \
    libjpeg-turbo-dev && \
    docker-php-ext-configure gd \
      --with-freetype=/usr/include/ \
      --with-jpeg=/usr/include/ && \
    #curl iconv session
    curl -L -o /tmp/memcached.tar.gz http://pecl.php.net/get/memcached-3.1.5.tgz &&\
    tar -xzvf /tmp/memcached.tar.gz &&\
    mv memcached-3.1.5 /usr/src/php/ext/memcached &&\
    rm /tmp/memcached.tar.gz &&\
    docker-php-ext-install pdo_mysql pdo_sqlite mysqli gd exif intl xsl json soap dom zip opcache memcached && \
    docker-php-source delete && \
    mkdir -p /var/log/supervisor && \
    echo "Asia/Shanghai" >  /etc/timezone &&\
    EXPECTED_COMPOSER_SIGNATURE=$(wget -q -O - https://composer.github.io/installer.sig) && \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '${EXPECTED_COMPOSER_SIGNATURE}') { echo 'Composer.phar Installer verified'; } else { echo 'Composer.phar Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php --install-dir=/usr/bin --filename=composer && \
    php -r "unlink('composer-setup.php');"  && \
    #pip install -U pip && \
    #pip install -U certbot && \
    #mkdir -p /etc/letsencrypt/webrootauth && \
    apk del gcc musl-dev linux-headers libffi-dev augeas-dev python-dev &&\
    rm -rf /usr/src


#############3 tweak php-fpm config##################
RUN echo "cgi.fix_pathinfo=0" > ${php_vars} &&\
    echo "upload_max_filesize = 100M"  >> ${php_vars} &&\
    echo "post_max_size = 100M"  >> ${php_vars} &&\
    echo "variables_order = \"EGPCS\""  >> ${php_vars} && \
    echo "memory_limit = 128M"  >> ${php_vars} && \
    sed -i \
        -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" \
        -e "s/pm.max_children = 5/pm.max_children = 20/g" \
        -e "s/pm.start_servers = 2/pm.start_servers = 10/g" \
        -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 5/g" \
        -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 20/g" \
        -e "s/;pm.max_requests = 500/pm.max_requests = 200/g" \
        -e "s/user = www-data/user = www/g" \
        -e "s/group = www-data/group = www/g" \
        -e "s/;listen.mode = 0660/listen.mode = 0666/g" \
        -e "s/;listen.owner = www-data/listen.owner = www/g" \
        -e "s/;listen.group = www-data/listen.group = www/g" \
        -e "s/listen = 127.0.0.1:9000/listen = \/tmp\/php-cgi.sock/g" \
        -e "s/^;clear_env = no$/clear_env = no/" \
        ${fpm_conf}

ADD start.sh /start.sh
ADD supervisord.conf /etc/supervisord.conf
RUN chmod 755 /start.sh

EXPOSE 80/tcp 443/tcp
CMD ["/start.sh"]
