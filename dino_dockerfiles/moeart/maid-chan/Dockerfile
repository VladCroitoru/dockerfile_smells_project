FROM debian:9-slim
MAINTAINER MoeArt Developmemnt Team <dev@art.moe>

#////////////////////////////////////////////////////////////////////
#//                                  ______
#//     ____ _  _____   ____ _  ____/ /   _____  ____ _ _      ____
#//   / __ `/ / ___/  / __ `/ / __  /   / ___/ / __ `/| | /| / /
#//  / /_/ / / /__   / /_/ / / /_/ /   / /    / /_/ / | |/ |/ /
#//  \__,_/  \___/   \__, /  \__,_/   /_/     \__,_/  |__/|__/
#//                 /____/
#//
#////////////////////////////////////////////////////////////////////

#########################
##                     ##
##     S Y S T E M     ##
##                     ##
#########################
# initize debian base system
ENV MAID_CHAN_USER www-data
ENV MAID_CHAN_OPENSSL 1.0.2o
ENV DEBIAN_FRONTEND noninteractive
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL C

# initize debian software source
# and base packages
RUN mkdir -p /usr/src && \
    #sed -i 's|deb.debian.org|mirrors.ustc.edu.cn|g' /etc/apt/sources.list && \
    #sed -i 's|security.debian.org/debian-security|mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y \
    cron \
    build-essential \
    libpcre3-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    libgd-dev \
    libgeoip-dev \
    libperl-dev \
    zlib1g-dev

# configure timezone and locale
# set to Asia/Chongqing
RUN ln -snf /usr/share/zoneinfo/Asia/Chongqing /etc/localtime && \
    echo Asia/Chongqing > /etc/timezone



#########################
##                     ##
##    T E N G I N E    ##
##                     ##
#########################
WORKDIR /usr/src
ADD https://github.com/alibaba/tengine/archive/master.tar.gz tengine.tar.gz
ADD https://www.openssl.org/source/openssl-$MAID_CHAN_OPENSSL.tar.gz openssl.tar.gz
RUN tar -zxvf tengine.tar.gz && \
    tar -zxvf openssl.tar.gz && \
    cd tengine-master && \
    sed -i " \
        /#define TENGINE.*/s/\"Tengine/\"MoeArt Maid-chan/; \
        /#define tengine_version.*/s/[0-9]\{7\}/`date +%y%m0%d`/; \
        /#define TENGINE_VERSION.*/s/\".*\"/\"`date +%y.%m.%d`\"/; \
        /#define NGINX_VER.*/s/\"nginx/\"MoeArt Maid-chan/; \
        /#define NGINX_VAR.*/s/\"NGINX/\"MoeArt Maid-chan/; \
        " src/core/nginx.h && \
    sed -i " \
        s/ Sorry for the inconvenience./ And, Maid-chan donot know what you need./; \
        s/Please report this message and include the following information to us./Please report this message and include the following information to Maid-chan./; \
        s/Thank you very much/Inconvenience to you my sincere apologies/; \
        s/<hr><center>tengine<\/center>//; \
        s/<center>//; \
        s/<\/center>//; \
        " src/http/ngx_http_special_response.c && \
    ./configure \
        --user=$MAID_CHAN_USER \
        --group=$MAID_CHAN_USER \
        --prefix=/usr/share/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --lock-path=/var/lock/nginx.lock \
        --pid-path=/run/nginx.pid \
        --http-client-body-temp-path=/var/lib/nginx/body \
        --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
        --http-proxy-temp-path=/var/lib/nginx/proxy \
        --http-scgi-temp-path=/var/lib/nginx/scgi \
        --http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
        --with-openssl=/usr/src/openssl-$MAID_CHAN_OPENSSL \
        --with-http_ssl_module \
        --with-http_gzip_static_module \
        --with-http_gunzip_module \
        --with-md5=/usr/include/openssl \
        --with-sha1-asm \
        --with-md5-asm \
        --with-http_auth_request_module \
        --with-http_image_filter_module \
        --with-http_addition_module \
        --with-http_realip_module \
        --with-http_v2_module \
        --with-http_ssl_module \
        --with-http_stub_status_module \
        --with-http_sub_module \
        --with-http_xslt_module \
        --with-http_mp4_module \
        --with-http_degradation_module \
        --with-ipv6 \
        --with-file-aio \
        --with-pcre \
        --with-pcre-jit \
        --without-http_upstream_keepalive_module \
        --add-module=modules/ngx_http_slice_module \
        --add-module=modules/ngx_http_sysguard_module \
        --add-module=modules/ngx_http_concat_module \
        --add-module=modules/ngx_http_footer_filter_module \
        --add-module=modules/ngx_http_trim_filter_module \
        --add-module=modules/ngx_http_upstream_check_module \
        --add-module=modules/ngx_http_upstream_consistent_hash_module \
        --add-module=modules/ngx_http_upstream_dynamic_module \
        --add-module=modules/ngx_http_upstream_dyups_module \
        --add-module=modules/ngx_http_upstream_keepalive_module \
        --add-module=modules/ngx_http_upstream_session_sticky_module \
        --add-module=modules/ngx_http_user_agent_module \
        --prefix=/etc/nginx \
        --http-log-path=/var/log/nginx/access.log \
        --error-log-path=/var/log/nginx/error.log \
        --sbin-path=/usr/sbin/nginx && \
    make && \
    make install && \
    mkdir -p /var/cache/nginx && \
    mkdir -p /var/ngx_pagespeed_cache && \
    mkdir -p /var/log/pagespeed && \
    mkdir -p /etc/nginx/conf.d && \
    mkdir -p /etc/nginx/sites-available && \
    mkdir -p /etc/nginx/sites-enabled && \
    mkdir -p /var/lib/nginx/body && \
    mkdir -p /var/www && \
    chown -R $MAID_CHAN_USER:$MAID_CHAN_USER /var/cache/nginx && \
    chown -R $MAID_CHAN_USER:$MAID_CHAN_USER /var/ngx_pagespeed_cache && \
    chown -R $MAID_CHAN_USER:$MAID_CHAN_USER /var/log/nginx && \
    chown -R $MAID_CHAN_USER:$MAID_CHAN_USER /var/log/pagespeed && \
    chown -R $MAID_CHAN_USER:$MAID_CHAN_USER /etc/nginx/sites-available && \
    chown -R $MAID_CHAN_USER:$MAID_CHAN_USER /etc/nginx/sites-enabled && \
    chown -R $MAID_CHAN_USER:$MAID_CHAN_USER /var/lib/nginx/body && \
    chown -R $MAID_CHAN_USER:$MAID_CHAN_USER /var/www



#########################
##                     ##
##       P H P 7       ##
##                     ##
#########################
RUN apt-get install -y \
    php7.0-fpm \
    php7.0-common \
    php7.0-curl \
    php7.0-bcmath \
    php7.0-bz2 \
    php7.0-dba \
    php7.0-dom \
    php7.0-gd \
    php7.0-mbstring \
    php7.0-json \
    php7.0-mcrypt \
    php7.0-mysqlnd \
    php7.0-readline \
    php7.0-simplexml \
    php7.0-xml \
    php7.0-soap \
    php7.0-zip \
    php7.0-cli \
    php7.0-opcache \
    php7.0-imagick



#########################
##                     ##
##      C L E A N      ##
##                     ##
#########################
RUN apt-get remove -y build-essential && \
    apt-get autoremove -y && \
    apt-get clean all && \
    rm -rf /usr/src/* && \
    rm -rf /tmp/*



#########################
##                     ##
##       M A I D       ##
##                     ##
#########################
ADD conf/nginx.conf /etc/nginx/nginx.conf
ADD conf/mime.types /etc/nginx/mime.types
ADD conf/default /etc/nginx/sites-enabled/default
ADD conf/php.ini /etc/php/7.0/fpm/php.ini
ADD conf/fpm.ini /etc/php/7.0/fpm/pool.d/www.conf
ADD html/ /etc/nginx/html/
ADD script/maid /maid

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    chmod +x /maid

VOLUME ["/var/log/nginx"]

WORKDIR /etc/nginx
EXPOSE 80 443
CMD ["/maid"]
