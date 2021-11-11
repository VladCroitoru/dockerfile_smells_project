FROM greatbsky/centos7
MAINTAINER architect.bian
LABEL name="nginx-https" license="GPLv2" build-date="20161024"

ENV NGINX_VERSION 1.10.2
ENV CONFIG "--prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-http_ssl_module --with-http_realip_module --with-http_addition_module --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module --with-http_secure_link_module --with-http_stub_status_module --with-http_auth_request_module --with-threads --with-stream --with-stream_ssl_module --with-http_slice_module --with-mail --with-mail_ssl_module --with-file-aio --with-http_v2_module --with-ipv6 --with-pcre=/data/softs/pcre-8.37 --with-zlib=/data/softs/zlib-1.2.8"

RUN cd /data/softs && wget "http://jaist.dl.sourceforge.net/project/pcre/pcre/8.37/pcre-8.37.tar.gz" && tar -zxf pcre-8.37.tar.gz && cd pcre-8.37 && ./configure && make && make install && cd /data/softs && wget "http://zlib.net/zlib-1.2.8.tar.gz" && tar -zxf zlib-1.2.8.tar.gz && cd zlib-1.2.8 && ./configure && make && make install && groupadd -f nginx && useradd -g nginx nginx && mkdir /var/cache/nginx && rm -rf ./nginx-1.10.2.tar.gz && cd /data/softs && wget "http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz" && tar -zxf nginx-$NGINX_VERSION.tar.gz && cd nginx-$NGINX_VERSION && ./configure $CONFIG && make && make install

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]













