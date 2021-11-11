FROM debian:jessie
MAINTAINER togana o.togana@gmail.com

ENV NGINX_VERSION=1.10.0 \
    GOPATH=/go \
    PATH=/nginx/sbin:/go/bin:$PATH

WORKDIR /tmp/nginx

RUN apt-get update && \
    apt-get install -y  --no-install-recommends \
      ca-certificates \
      wget \
      git \
      mercurial \
      g++ \
      make \
      libpcre3-dev \
      libssl-dev \
      libxslt-dev \
      libxml2-dev \
      libgd2-xpm-dev \
      libgeoip-dev \
      libperl-dev \
      golang && \
    rm -rf /var/lib/apt/lists/* && \
    go get -u github.com/cubicdaiya/nginx-build

COPY modules /tmp/nginx
RUN mkdir -p /tmp/nginx/work && \
    nginx-build \
      -verbose \
      -v $NGINX_VERSION \
      -d work \
      --prefix=/etc/nginx \
      --sbin-path=/usr/sbin/nginx \
      --modules-path=/usr/lib/nginx/modules \
      --conf-path=/etc/nginx/nginx.conf \
      --error-log-path=/var/log/nginx/error.log \
      --http-log-path=/var/log/nginx/access.log \
      --pid-path=/var/run/nginx.pid \
      --lock-path=/var/run/nginx.lock \
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
      --with-http_geoip_module=dynamic \
      --with-http_perl_module=dynamic \
      --with-threads \
      --with-stream \
      --with-stream_ssl_module \
      --with-http_slice_module \
      --with-mail \
      --with-mail_ssl_module \
      --with-file-aio \
      --with-ipv6 \
      --with-http_v2_module \
      --with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2' \
      --with-ld-opt='-Wl,-z,relro -Wl,--as-needed' \
      -m modules && \
  cd work/nginx/$NGINX_VERSION/nginx-$NGINX_VERSION && \
  make install && \
  rm -rf /tmp/nginx/work && \
  groupadd nginx && \
  useradd -g nginx nginx && \
  usermod -s /bin/false nginx && \
  mkdir -p /var/cache/nginx/client_temp

ONBUILD COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
