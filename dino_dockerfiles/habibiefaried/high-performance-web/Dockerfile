FROM alpine:3.4

MAINTAINER habibiefaried@gmail.com

#Default Config, just change this
ENV MYSQL_ROOT_PASSWORD=admin2017!
ENV PHPMYADMIN_DIR=secretmysql
ENV PHPREDISADMIN_DIR=secretredis

ENV NGINX_VERSION=1.11.2 \
     PAGESPEED_VERSION=1.11.33.4 \
     LIBPNG_VERSION=1.2.56 \
     MAKE_J=4 \
     PAGESPEED_ENABLE=on

RUN apk upgrade --no-cache --update && \
    apk add --no-cache --update \
        bash \
        ca-certificates \
        libuuid \
        apr \
        apr-util \
        libjpeg-turbo \
        icu \
        icu-libs \
        openssl \
        pcre \
        zlib \
        git mysql mysql-client nano

RUN cd /root && git clone https://github.com/vozlt/nginx-module-vts.git && cd /
RUN adduser -D websrv && adduser -D phpfpm

RUN git clone https://github.com/nbs-system/naxsi.git "/root/nginx-naxsi"

COPY src/nginx/src/http/ngx_http_header_filter_module.c /root/ngx_http_header_filter_module.c
COPY src/nginx/src/core/nginx.h /root/nginx.h

RUN set -x && \
    apk --no-cache add -t .build-deps \
        apache2-dev \
        apr-dev \
        apr-util-dev \
        build-base \
        curl \
        icu-dev \
        libjpeg-turbo-dev \
        linux-headers \
        gperf \
        openssl-dev \
        pcre-dev \
        python \
        zlib-dev && \
    # Build libpng
    cd /tmp && \
    curl -L http://prdownloads.sourceforge.net/libpng/libpng-${LIBPNG_VERSION}.tar.gz | tar -zx && \
    cd /tmp/libpng-${LIBPNG_VERSION} && \
    ./configure --build=$CBUILD --host=$CHOST --prefix=/usr --enable-shared --with-libpng-compat && \
    make -j${MAKE_J} install V=0 && \
    # Build PageSpeed
    cd /tmp && \
    curl -L https://dl.google.com/dl/linux/mod-pagespeed/tar/beta/mod-pagespeed-beta-${PAGESPEED_VERSION}-r0.tar.bz2 | tar -jx && \
    curl -L https://github.com/pagespeed/ngx_pagespeed/archive/v${PAGESPEED_VERSION}-beta.tar.gz | tar -zx && \
    cd /tmp/modpagespeed-${PAGESPEED_VERSION} && \
    curl -L https://raw.githubusercontent.com/lagun4ik/docker-nginx-pagespeed/master/patches/automatic_makefile.patch | patch -p1 && \
    curl -L https://raw.githubusercontent.com/lagun4ik/docker-nginx-pagespeed/master/patches/libpng_cflags.patch | patch -p1 && \
    curl -L https://raw.githubusercontent.com/lagun4ik/docker-nginx-pagespeed/master/patches/pthread_nonrecursive_np.patch | patch -p1 && \
    curl -L https://raw.githubusercontent.com/lagun4ik/docker-nginx-pagespeed/master/patches/rename_c_symbols.patch | patch -p1 && \
    curl -L https://raw.githubusercontent.com/lagun4ik/docker-nginx-pagespeed/master/patches/stack_trace_posix.patch | patch -p1 && \
    ./generate.sh -D use_system_libs=1 -D _GLIBCXX_USE_CXX11_ABI=0 -D use_system_icu=1 && \
    cd /tmp/modpagespeed-${PAGESPEED_VERSION}/src && \
    make -j${MAKE_J} BUILDTYPE=Release CXXFLAGS=" -I/usr/include/apr-1 -I/tmp/libpng-${LIBPNG_VERSION} -fPIC -D_GLIBCXX_USE_CXX11_ABI=0" CFLAGS=" -I/usr/include/apr-1 -I/tmp/libpng-${LIBPNG_VERSION} -fPIC -D_GLIBCXX_USE_CXX11_ABI=0" && \
    cd /tmp/modpagespeed-${PAGESPEED_VERSION}/src/pagespeed/automatic/ && \
    make -j${MAKE_J} psol BUILDTYPE=Release CXXFLAGS=" -I/usr/include/apr-1 -I/tmp/libpng-${LIBPNG_VERSION} -fPIC -D_GLIBCXX_USE_CXX11_ABI=0" CFLAGS=" -I/usr/include/apr-1 -I/tmp/libpng-${LIBPNG_VERSION} -fPIC -D_GLIBCXX_USE_CXX11_ABI=0" && \
    mkdir -p /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol && \
    mkdir -p /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/lib/Release/linux/x64 && \
    mkdir -p /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/include/out/Release && \
    cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/out/Release/obj /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/include/out/Release/ && \
    cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/net /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/include/ && \
    cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/testing /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/include/ && \
    cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/pagespeed /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/include/ && \
    cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/third_party /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/include/ && \
    cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/tools /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/include/ && \
    cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/url /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/include/ && \
    cp -r /tmp/modpagespeed-${PAGESPEED_VERSION}/src/pagespeed/automatic/pagespeed_automatic.a /tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta/psol/lib/Release/linux/x64 && \
    # Build Nginx with support for PageSpeed
    cd /tmp && \
    curl -L http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar -zx && \
    cd /tmp/nginx-${NGINX_VERSION} && \
    rm /tmp/nginx-${NGINX_VERSION}/src/http/ngx_http_header_filter_module.c && \
    rm /tmp/nginx-${NGINX_VERSION}/src/core/nginx.h && \
    cp /root/ngx_http_header_filter_module.c /tmp/nginx-${NGINX_VERSION}/src/http/ngx_http_header_filter_module.c && \
    cp /root/nginx.h /tmp/nginx-${NGINX_VERSION}/src/core/nginx.h && \
    LD_LIBRARY_PATH=/tmp/modpagespeed-${PAGESPEED_VERSION}/usr/lib ./configure \
        --sbin-path=/usr/sbin \
        --modules-path=/usr/lib/nginx \
        --with-http_ssl_module \
        --with-http_gzip_static_module \
        --with-file-aio \
        --with-http_v2_module \
        --with-http_realip_module \
        --without-http_autoindex_module \
        --without-http_browser_module \
        --without-http_geo_module \
        --without-http_memcached_module \
        --without-http_userid_module \
        --without-mail_pop3_module \
        --without-mail_imap_module \
        --without-mail_smtp_module \
        --without-http_split_clients_module \
        --without-http_uwsgi_module \
        --without-http_scgi_module \
        --without-http_upstream_ip_hash_module \
        --with-http_sub_module \
        --with-http_gunzip_module \
        --with-http_secure_link_module \
        --with-threads \
        --with-stream \
        --with-stream_ssl_module \
        --prefix=/etc/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --http-log-path=/var/log/nginx/access.log \
        --error-log-path=/var/log/nginx/error.log \
        --pid-path=/var/run/nginx.pid \
        --add-module=/tmp/ngx_pagespeed-${PAGESPEED_VERSION}-beta \
        --add-module=/root/nginx-module-vts \
        --add-module="/root/nginx-naxsi/naxsi_src" \
        --with-cc-opt="-fPIC -I /usr/include/apr-1" \
        --with-ld-opt="-luuid -lapr-1 -laprutil-1 -licudata -licuuc -L/tmp/modpagespeed-${PAGESPEED_VERSION}/usr/lib -lpng12 -lturbojpeg -ljpeg" && \
    make -j${MAKE_J} install --silent && \
    # Clean-up
    cd && \
    apk del .build-deps && \
    rm -rf /tmp/* && \
    # Forward request and error logs to docker log collector
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    # Make PageSpeed cache writable
    mkdir -p /var/cache/ngx_pagespeed /var/log/pagespeed && \
    chmod -R 777 /var/cache/ngx_pagespeed && chmod -R 777 /var/log/pagespeed \
    && rm -rf /etc/nginx/html/ \
    && mkdir -p /usr/share/nginx/html/ 

##Instal php5-fpm
RUN apk add --update \
		php5-mcrypt \
		php5-soap \
		php5-openssl \
		php5-gmp \
		php5-pdo_odbc \
		php5-json \
		php5-dom \
		php5-pdo \
		php5-zip \
		php5-mysql \
        php5-mysqli \
		php5-sqlite3 \
		php5-apcu \
		php5-intl \
		php5-imagick \
		php5-pdo_pgsql \
		php5-pgsql \
		php5-bcmath \
		php5-gd \
		php5-xcache \
		php5-mcrypt \
		php5-ldap \
		php5-odbc \
		php5-pdo_mysql \
		php5-pdo_sqlite \
		php5-gettext \
		php5-xmlreader \
		php5-xmlrpc \
		php5-bz2 \
		php5-memcache \
		php5-mssql \
		php5-iconv \
		php5-pdo_dblib \
		php5-curl \
		php5-ctype \
		php5-dev \  
		php5-common \
		php5-pear \
		php5-xml \
		php5-wddx \
		php5-xsl \
		php5-ftp \
		php5-phar \
		php5-posix \
		php5-shmop \
		php5-soap \
		php5-sockets \
		php5-sqlite3 \
		php5-zlib \
		php5-phpmailer \
		php5-zip \
		php5-exif \
		php5-phpdbg \
		php5-opcache \
		php5-fpm


##PECL
RUN apk add --no-cache bash build-base wget curl m4 autoconf libtool imagemagick imagemagick-dev zlib zlib-dev libcurl curl-dev libevent libevent-dev libidn libmemcached libmemcached-dev libidn-dev && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN sed -i "$ s|\-n||g" /usr/bin/pecl
RUN echo "extension=iconv.so" >> /etc/php5/php.ini
RUN printf "\n" | pecl install raphf-1.1.2 propro-1.0.2 
RUN echo "extension=raphf.so" >> /etc/php5/php.ini
RUN echo "extension=propro.so" >> /etc/php5/php.ini
RUN printf "\n" | pecl install pecl_http-2.5.6
RUN echo "extension=http.so" >> /etc/php5/php.ini
RUN printf "\n" | pecl install redis

COPY config/conf.d /etc/nginx/conf.d
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY html /usr/share/nginx/html
COPY config/naxsi /etc/nginx/naxsi
COPY init.sh /init.sh
RUN chmod +x /init.sh
VOLUME ["/var/cache/ngx_pagespeed","/app"]
COPY my.cnf /etc/mysql/my.cnf

COPY php-fpm.conf /etc/php5/php-fpm.conf
COPY php.ini /etc/php5/php.ini
RUN chmod -R 777 /var/log/

RUN echo "export TERM=xterm" > /root/.bashrc
RUN echo 'PS1="\[\033[35m\]\t\[\033[m\]-\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "' >> /root/.bashrc

WORKDIR /tmp
RUN apk add --update redis
RUN wget https://files.phpmyadmin.net/phpMyAdmin/4.6.6/phpMyAdmin-4.6.6-all-languages.zip && unzip phpMyAdmin-4.6.6-all-languages.zip
RUN mv phpMyAdmin-4.6.6-all-languages /usr/share/nginx/html/$PHPMYADMIN_DIR
RUN git clone https://github.com/ErikDubbelboer/phpRedisAdmin.git && cd phpRedisAdmin && git submodule init && git submodule update && cd ..
RUN mv phpRedisAdmin /usr/share/nginx/html/$PHPREDISADMIN_DIR

RUN cd /usr/share/nginx/html/$PHPREDISADMIN_DIR && composer install
WORKDIR /root
CMD ["/init.sh"]