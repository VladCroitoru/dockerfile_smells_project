FROM ubuntu:xenial
ENV NGX_VER 1.15.9   
RUN sed -i "/^# deb-src/ s/^# //" /etc/apt/sources.list; \
    apt-get update ; \
    apt-get dist-upgrade -y ; \
    apt-get install -y wget libgoogle-perftools-dev vim-tiny; \
    apt-get build-dep nginx -y;\
    wget http://nginx.org/download/nginx-${NGX_VER}.tar.gz; \
    tar zxvf nginx-${NGX_VER}.tar.gz ;\
    cd nginx-${NGX_VER}; \
    ./configure --prefix=/usr/local/nginx --sbin-path=/usr/local/nginx/sbin/nginx --conf-path=/usr/local/nginx/etc/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --http-client-body-temp-path=/tmp/nginx/client_body --http-proxy-temp-path=/tmp/nginx/proxy --http-fastcgi-temp-path=/tmp/nginx/fastcgi --http-uwsgi-temp-path=/tmp/nginx/uwsgi --http-scgi-temp-path=/tmp/nginx/scgi --pid-path=/run/nginx.pid --lock-path=/run/lock/subsys/nginx --user=nginx --group=nginx --with-file-aio --with-ipv6 --with-http_ssl_module  --with-http_realip_module --with-http_addition_module --with-http_xslt_module --with-http_image_filter_module --with-http_geoip_module --with-http_sub_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_random_index_module --with-http_secure_link_module --with-http_degradation_module --with-http_stub_status_module --with-http_perl_module --with-mail --with-mail_ssl_module --with-pcre --with-pcre-jit --with-google_perftools_module --with-debug --with-threads  --with-http_v2_module --with-cc-opt=" -Ofast " ;\
    make ; make install; \
    useradd nginx;\
    rm -rf /var/lib/apt/lists/*;\
    cd ..;\
    rm -rf nginx-${NGX_VER};
    

ENV TERM xterm
VOLUME ["/tmp/nginx"]

ENV HOME /root
ENV PATH="/usr/local/nginx/bin:/usr/local/nginx/sbin:${PATH}"
WORKDIR /root

COPY nginx.conf /usr/local/nginx/etc/nginx.conf
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]




