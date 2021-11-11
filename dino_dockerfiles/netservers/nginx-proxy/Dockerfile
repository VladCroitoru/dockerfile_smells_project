FROM debian:jessie
MAINTAINER John McEleney john.mceleney@netservers.co.uk

ENV \
  NGINX_VERSION=1.9.5 \
  OPENSSL_VERSION=openssl-1.0.2d \
  MODULESDIR=/usr/src/nginx-modules \
  NPS_VERSION=1.9.32.10 \
  DEBIAN_FRONTEND=noninteractive

EXPOSE 80 443

RUN apt-get update \
  && apt-get upgrade --yes \
  && apt-get install -y -q --no-install-recommends \
    ca-certificates \
    git \
    build-essential \
    perl \
    cmake \
    libpcre3 \
    libpcre3-dev \
    libperl-dev \
    zlib1g-dev \
    libluajit-5.1-dev \
    libldap2-dev \
    unzip \
    wget \
    curl \
  && mkdir -p ${MODULESDIR} \
  && mkdir -p /data/{config,ssl,logs} \
  && cd /usr/src/ \
  && curl http://www.openssl.org/source/${OPENSSL_VERSION}.tar.gz | tar zvx \
  && curl http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar zvx \
  && cd ${MODULESDIR} \
  && git clone git://github.com/bpaquet/ngx_http_enhanced_memcached_module.git \
  && git clone https://github.com/openresty/headers-more-nginx-module.git \
  && git clone https://github.com/openresty/redis2-nginx-module.git \
  && git clone https://github.com/openresty/lua-nginx-module.git \
  && git clone https://github.com/kvspb/nginx-auth-ldap.git \ 
  && wget https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_VERSION}-beta.zip \
  && unzip release-${NPS_VERSION}-beta.zip \
  && cd ngx_pagespeed-release-${NPS_VERSION}-beta/ \
  && curl -L -k https://dl.google.com/dl/page-speed/psol/${NPS_VERSION}.tar.gz | tar zxv \
  && cd /usr/src/nginx-${NGINX_VERSION} \
  && ./configure \
        --prefix=/etc/nginx \
        --user=nginx \
        --sbin-path=/usr/sbin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --pid-path=/var/run/nginx.pid \
        --lock-path=/var/run/nginx.lock \
        --with-http_ssl_module \
        --with-http_perl_module \
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
        --with-mail \
        --with-mail_ssl_module \
        --with-file-aio \
        --with-http_v2_module \
        --with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Wformat-security -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2' \
        --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,--as-needed' \
        --with-ipv6 \
        --with-sha1="../${OPENSSL_VERSION}" \
        --with-md5="../${OPENSSL_VERSION}" \
        --with-openssl="../${OPENSSL_VERSION}" \
        --add-module=${MODULESDIR}/ngx_pagespeed-release-${NPS_VERSION}-beta \
        --add-module=${MODULESDIR}/ngx_http_enhanced_memcached_module \
        --add-module=${MODULESDIR}/headers-more-nginx-module \
        --add-module=${MODULESDIR}/redis2-nginx-module \
        --add-module=${MODULESDIR}/lua-nginx-module \
        --add-module=${MODULESDIR}/nginx-auth-ldap \
  && cd /usr/src/nginx-${NGINX_VERSION} \
  && make \
  && make install \
  && cd / \
  && rm -fR /etc/nginx/* \
  && rm -fR /usr/src/* \
  && useradd -r -c "nginx user" -d /nonexistent -s /bin/false nginx \
  && apt-get purge -y \
    build-essential \
    cmake \
    unzip \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -r /var/lib/apt/lists/*

COPY nginx-conf /etc/nginx

# Configure Nginx and apply fix for very long server names
RUN echo "daemon off;" >> /etc/nginx/nginx.conf \
 && sed -i 's/^http {/&\n    server_names_hash_bucket_size 128;/g' /etc/nginx/nginx.conf

# Install Forego
RUN wget -P /usr/local/bin https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-amd64/forego \
 && chmod u+x /usr/local/bin/forego

ENV DOCKER_GEN_VERSION 0.4.2

RUN wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz

COPY . /app/
WORKDIR /app/

ENV DOCKER_HOST unix:///tmp/docker.sock

VOLUME ["/etc/nginx/certs"]

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["forego", "start", "-r"]
