FROM centos:7.3.1611

ENV RUBY_MAJOR_VERSION 2.4
ENV RUBY_FULL_VERSION 2.4.0
ENV NGX_MRUBY_VERSION v1.18.8

ENV NGINX_CONFIG_OPT_ENV --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module

RUN yum install -y git wget gcc make gcc-c++ bison openssl-devel zlib-devel

RUN cd /usr/local/src && \
  curl -O http://cache.ruby-lang.org/pub/ruby/${RUBY_MAJOR_VERSION}/ruby-${RUBY_FULL_VERSION}.tar.gz && \
  tar xvf ruby-${RUBY_FULL_VERSION}.tar.gz && \
  cd ruby-${RUBY_FULL_VERSION} && \
  ./configure --prefix /usr/local/ruby && \
  make && \
  make install

ENV PATH /usr/local/ruby/bin:${PATH}

RUN yum install -y http://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm && \
  yum install -y mysql-devel

RUN yum install -y libmemcached-devel

RUN git clone --depth=1 --branch=$NGX_MRUBY_VERSION https://github.com/matsumoto-r/ngx_mruby.git /usr/local/src/ngx_mruby && \
  cd /usr/local/src/ngx_mruby && \
  sed -i -e '/matsumotory\/mruby-memcached/s/#//' build_config.rb && \
  sed -i -e '/mattn\/mruby-mysql/s/#//' build_config.rb && \
  sh build.sh && \
  make install

RUN mkdir /var/cache/nginx

RUN yum clean all && \
  rm -rf /usr/local/src/ruby-${RUBY_FULL_VERSION}* && \
  rm -rf /usr/local/src/ngx_mruby

EXPOSE 80 443

ONBUILD ADD docker/hook.d /etc/nginx/hook.d
ONBUILD ADD docker/conf.d /etc/nginx/conf.d
ONBUILD ADD docker/nginx.conf /etc/nginx/nginx.conf

CMD ["/usr/sbin/nginx", "-g", "daemon off;"]
