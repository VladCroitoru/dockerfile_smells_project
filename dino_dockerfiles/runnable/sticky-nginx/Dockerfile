FROM ubuntu:14.04
MAINTAINER Bryan Kendall <bryan@runnable.com>

# Expose volumes for nginx
VOLUME [ "/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html" ]

# Install required packages for building nginx
RUN apt-get update && \
    apt-get install -y libpcre3-dev build-essential libssl-dev libperl-dev libxslt-dev libgd2-xpm-dev libgeoip-dev git wget && \
    rm -rf /var/lib/apt/lists/*

# Get all necessary resources
WORKDIR /nginx-src
RUN wget http://nginx.org/download/nginx-1.8.1.tar.gz && tar xzf nginx-1.8.1.tar.gz && rm -f nginx-1.8.1.tar.gz
RUN wget http://zlib.net/zlib-1.2.11.tar.gz && tar xzf zlib-1.2.11.tar.gz && rm -f zlib-1.2.11.tar.gz
RUN wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.39.tar.gz && tar xzf pcre-8.39.tar.gz && rm -f pcre-8.39.tar.gz
RUN wget https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng/get/1.2.6.tar.gz && tar xzf 1.2.6.tar.gz && rm -f 1.2.6.tar.gz

# Build nginx
WORKDIR /nginx-src/nginx-1.8.1/
RUN ./configure --with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2' \
                --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro' \
                --prefix=/usr/share/nginx \
                --conf-path=/etc/nginx/nginx.conf \
                --http-log-path=/var/log/nginx/access.log \
                --error-log-path=/var/log/nginx/error.log \
                --lock-path=/var/lock/nginx.lock \
                --pid-path=/run/nginx.pid \
                --http-client-body-temp-path=/var/lib/nginx/body \
                --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
                --http-proxy-temp-path=/var/lib/nginx/proxy \
                --http-scgi-temp-path=/var/lib/nginx/scgi \
                --http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
                --with-debug \
                --with-pcre-jit \
                --with-ipv6 \
                --with-http_ssl_module \
                --with-http_stub_status_module \
                --with-http_realip_module \
                --with-http_addition_module \
                --with-http_dav_module \
                --with-http_geoip_module \
                --with-http_gzip_static_module \
                --with-http_image_filter_module \
                --with-http_spdy_module \
                --with-http_sub_module \
                --with-http_xslt_module \
                --with-mail \
                --with-mail_ssl_module \
                --add-module=/nginx-src/nginx-goodies-nginx-sticky-module-ng-c78b7dd79d0d \
                --with-pcre=/nginx-src/pcre-8.39 \
                --with-zlib=/nginx-src/zlib-1.2.11

RUN make

RUN make install

# Extra settings to make nginx happier to work with
WORKDIR /etc/nginx
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN mkdir -p /var/lib/nginx/body
ENV PATH=/usr/share/nginx/sbin:$PATH
CMD [ "nginx" ]
EXPOSE 80
EXPOSE 443
