FROM debian

ENV NGINX_Version=1.13.9

WORKDIR /tmp

COPY www.zip /tmp/

RUN mkdir /usr/local/v2ray \
        && echo 'deb-src http://deb.debian.org/debian stretch main\ndeb-src http://deb.debian.org/debian stretch-updates main\ndeb-src http://security.debian.org stretch/updates main' >> /etc/apt/sources.list \ 
        && apt update \
        && apt install -y locales \
        && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8 \
        && apt -y install curl wget unzip procps net-tools git devscripts gdebi build-essential \
        && curl -s https://api.github.com/repos/v2ray/v2ray-core/releases/latest \
            | grep browser_download_url \
            | grep linux-64 \
            | cut -d '"' -f 4 \
            | wget -qi - \
        && unzip -jqo v2ray-linux-64.zip -d /usr/local/v2ray \
        && mk-build-deps nginx \
        && gdebi --option=APT::Get::force-yes=1,APT::Get::Assume-Yes=1 -n nginx*.deb \
        && git clone https://github.com/openssl/openssl.git \
        && curl http://nginx.org/download/nginx-$NGINX_Version.tar.gz | tar xvz \
        && cd nginx-$NGINX_Version \
        && ./configure --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=root --group=root --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-openssl='/tmp/openssl' --with-openssl-opt=enable-tls1_3 --with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fPIC' --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie' \
        && sed -i 's/-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie -ldl -lpthread -lpthread -lcrypt -lpcre \/tmp\/openssl\/\.openssl\/lib\/libssl\.a \/tmp\/openssl\/\.openssl\/lib\/libcrypto\.a -ldl -lz /-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie -ldl -lcrypt -lpcre \/tmp\/openssl\/\.openssl\/lib\/libssl\.a \/tmp\/openssl\/\.openssl\/lib\/libcrypto\.a -ldl -lz -lpthread /g' objs/Makefile \
        && make \
        && make install \
        && mkdir /var/cache/nginx \
        && mkdir /etc/nginx/proxy.d \
        && unzip /tmp/www.zip -d /root \
        && mkdir /var/log/v2ray \
        && apt -y remove locales curl wget unzip procps net-tools git devscripts gdebi nginx-build-deps build-essential \
        && apt-mark manual sudo \
        && apt -y autoremove \
        && rm -rf /var/lib/apt/lists/* \
        && rm -rf /tmp/*

COPY server.json /usr/local/v2ray/

COPY nginx.conf /etc/nginx/

COPY v2ray.conf /etc/nginx/conf.d/

COPY key.pem cert.pem /etc/nginx/ssl/

COPY wrapper.sh /root/

WORKDIR /root

CMD ["./wrapper.sh"]

EXPOSE 443

