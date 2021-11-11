FROM ubuntu:16.04
MAINTAINER cloverstd https://github.com/cloverstd

#COPY aliyun.sources.list /etc/apt/sources.list
RUN set -ex && \
    apt-get update -qq && \
    apt-get install -y --no-install-recommends build-essential libpcre3 libpcre3-dev zlib1g-dev unzip git autoconf libtool automake wget && \
    mkdir /tmp/src && cd /tmp/src && \
    wget --no-check-certificate -O nginx-ct.zip -c https://github.com/grahamedgecombe/nginx-ct/archive/v1.3.2.zip && \
    unzip nginx-ct.zip && \
    git config --global http.sslVerify false && \
    git clone https://github.com/bagder/libbrotli && \
    cd libbrotli && \
    ./autogen.sh && ./configure && \
    mkdir -p brotli/c/tools/.deps && touch brotli/c/tools/.deps/brotli-brotli.Po && \
    make && make install && cd ../ && \
    ln -s /usr/local/lib/libbrotlienc.so.0 /usr/lib/libbrotlienc.so.0 && \
    git clone https://github.com/google/ngx_brotli.git && \
    cd ngx_brotli && git submodule update --init && cd ../ && \
    git clone https://github.com/cloudflare/sslconfig.git && \
    wget --no-check-certificate -O openssl.tar.gz -c https://github.com/openssl/openssl/archive/OpenSSL_1_0_2k.tar.gz && \
    tar zxf openssl.tar.gz && \
    mv openssl-OpenSSL_1_0_2k/ openssl && \
    cd openssl && patch -p1 < ../sslconfig/patches/openssl__chacha20_poly1305_draft_and_rfc_ossl102j.patch && cd ../ && \
    wget --no-check-certificate -c https://nginx.org/download/nginx-1.11.13.tar.gz && \
    tar zxf nginx-1.11.13.tar.gz && \
    cd nginx-1.11.13/ && \
    patch -p1 < ../sslconfig/patches/nginx__1.11.5_dynamic_tls_records.patch && \
    ./configure --add-module=../ngx_brotli --add-module=../nginx-ct-1.3.2 --with-openssl=../openssl --with-http_v2_module --with-http_ssl_module --with-http_gzip_static_module && \
    make  && make install && \
    rm -rf /tmp/src && apt-get remove -y unzip git autoconf libtool wget automake build-essential


# forward request and error logs to docker log collector
# from https://github.com/nginxinc/docker-nginx
RUN ln -sf /dev/stdout /usr/local/nginx/logs/access.log \
	&& ln -sf /dev/stderr /usr/local/nginx/logs/error.log

EXPOSE 80 443

CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]
