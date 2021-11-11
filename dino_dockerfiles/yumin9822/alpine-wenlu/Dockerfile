FROM alpine:edge
MAINTAINER yumin9822 <yumin9822@gmail.com>

# Install alpine base development environmental package.
RUN apk update && \
    apk add alpine-sdk && \
    apk add git wget gcc g++ make zlib-dev pcre-dev openssl-dev perl-dev

# Get Source Code
RUN \
  cd /tmp && \
  wget "http://nginx.org/download/nginx-1.10.1.tar.gz" && \
  wget "http://linux.stanford.edu/pub/exim/pcre/pcre-8.38.tar.gz" && \
  wget "https://www.openssl.org/source/openssl-1.0.2h.tar.gz" && \
  wget "http://zlib.net/zlib-1.2.8.tar.gz" && \
  git clone https://github.com/cuber/ngx_http_google_filter_module && \
  git clone https://github.com/yaoweibin/ngx_http_substitutions_filter_module && \
  tar xzvf nginx-1.10.1.tar.gz && \
  tar xzvf pcre-8.38.tar.gz && \
  tar xzvf openssl-1.0.2h.tar.gz && \
  tar xzvf zlib-1.2.8.tar.gz

# Install Nginx
RUN \
  cd /tmp/nginx-1.10.1 && \
  ./configure --prefix=/opt/nginx --with-pcre=/tmp/pcre-8.38 --with-openssl=/tmp/openssl-1.0.2h --with-zlib=/tmp/zlib-1.2.8 --with-http_ssl_module --add-module=/tmp/ngx_http_google_filter_module --add-module=/tmp/ngx_http_substitutions_filter_module && \
  make && make install

RUN rm -rf /var/cache/apk/* && rm -rf /tmp

# Run Nginx
ADD ./nginx.conf /opt/nginx/conf/nginx.conf

EXPOSE 80
# EXPOSE 443

WORKDIR /opt/nginx/sbin

CMD ["./nginx", "-g", "daemon off;"]

