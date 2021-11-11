# Build nginx with Docker

FROM justincormack/frankenlibc

MAINTAINER Justin Cormack

RUN cd /usr/src && curl http://nginx.org/download/nginx-1.9.2.tar.gz | tar xfz -

WORKDIR /usr/src/nginx-1.9.2

ENV CC=rumprun-cc

# make uname the NetBSD one
RUN cd /usr/local/bin && ln -s rump.uname uname

RUN ./configure \
  --conf-path=/data/conf/nginx.conf \
  --sbin-path=/none \
  --pid-path=/tmp/nginx.pid \
  --lock-path=/tmp/nginx.lock \
  --error-log-path=/tmp/error.log \
  --http-log-path=/tmp/access.log \
  --http-client-body-temp-path=/tmp/client-body \
  --http-proxy-temp-path=/tmp/proxy \
  --http-fastcgi-temp-path=/tmp/fastcgi \
  --http-scgi-temp-path=/tmp/scgi \
  --http-uwsgi-temp-path=/tmp/uwsgi \
  --without-http_rewrite_module \
  --with-ipv6 \
  && \
  make && cp objs/nginx /usr/local/bin && make clean 
