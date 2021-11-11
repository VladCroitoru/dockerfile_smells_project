FROM debian

ENV NGINX_VERSION 1.9.11
ENV NGINX_LUA 0.10.1rc1
ENV NGINX_DEV_KIT 0.2.19
ENV CONFD_VERSION 0.11.0
ENV CONSUL_TPL_VERSION 0.10.0

ENV LUA_LIB /usr/lib/
ENV LUA_INC /usr/include/lua5.1

RUN export buildDeps=' \
    build-essential \
    liblua5.1-0-dev \
    lua-sec-dev \
    git \
    libffi-dev \
    python3-dev \
    python3-pip \
    ' && \
    apt-get update && \
    apt-get install --no-install-recommends --fix-missing -y $buildDeps \
    runit \
    python3 \
    python3-six \
    python3-urllib3 \
    curl \
    libpcre3 libpcre3-dev libssl-dev liblwp-useragent-determined-perl libpam0g-dev \
    lua5.1 \
    lua-sec \
    liblua5.1-0 \
    lua-json && \
    adduser --system --no-create-home --disabled-login --group --disabled-password nginx && \
    curl -sSL https://github.com/hashicorp/consul-template/archive/v0.10.0.tar.gz -o consul-template_${CONSUL_TPL_VERSION}_linux_amd64.tar.gz && \
    tar -xf consul-template_${CONSUL_TPL_VERSION}_linux_amd64.tar.gz  -C /usr/local/bin --strip-components=1 && \
    rm consul-template_${CONSUL_TPL_VERSION}_linux_amd64.tar.gz && \
    curl -sSL https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 -o /usr/local/bin/confd && \
    chmod +x /usr/local/bin/confd && \
    curl -sSL https://github.com/chaoslawful/lua-nginx-module/archive/v${NGINX_LUA}.tar.gz -o /usr/src/lua-nginx-module.tar.gz && \
    tar -xf /usr/src/lua-nginx-module.tar.gz -C /usr/src && \
    curl -sSL https://github.com/simpl/ngx_devel_kit/archive/v${NGINX_DEV_KIT}.tar.gz -o /usr/src/ngx_devel_kit.tar.gz && \
    tar -xf /usr/src/ngx_devel_kit.tar.gz -C /usr/src && \
    curl -sSL http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -o /usr/src/nginx-${NGINX_VERSION}.tar.gz && \
    tar -xf /usr/src/nginx-${NGINX_VERSION}.tar.gz  -C /usr/src && \
    ln -s `find /usr/lib -iname liblua5.1.so` /usr/lib/liblua.so && \
    cd /usr/src/nginx-${NGINX_VERSION} && \
    CC=/usr/bin/gcc ./configure \
        --prefix=/usr/share/nginx \
        --sbin-path=/usr/sbin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --pid-path=/var/run/nginx.pid \
        --lock-path=/var/lock/nginx.lock \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --user=nginx \
        --group=nginx \
        --without-mail_pop3_module \
        --without-mail_imap_module \
        --without-mail_smtp_module \
        --without-http_uwsgi_module \
        --without-http_scgi_module \
        --with-ipv6 \
        --with-stream \
        --with-http_ssl_module \
        --with-http_v2_module \
        --with-http_stub_status_module \
        --with-http_gzip_static_module \
        --add-module=/usr/src/ngx_devel_kit-${NGINX_DEV_KIT} \
        --add-module=/usr/src/lua-nginx-module-${NGINX_LUA} && \
    make && \
    make install && \
    git clone https://github.com/agoragames/nginx-google-oauth /usr/src/nginx-google-oauth && \
    cp /usr/src/nginx-google-oauth/*.lua /etc/nginx/ && \
    pip3 install pynacl pyopenssl && \
    git clone https://github.com/jplana/python-etcd.git && \
    cd python-etcd && \
    python3 setup.py install && \
    cd .. && rm -rf python-etcd && \ 
    apt-get install -y mysql-client && \   
    apt-get -y purge --auto-remove $buildDeps && \
    apt-get clean && rm -rf /usr/src/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD tpl.confd /tpl.confd
#ADD tpl.consul /tpl.consul

ADD my_init/my_init /sbin/my_init
ADD 2.sh /etc/runit/2

#ADD ./my_init.d /etc/my_init.d
ADD ./service /etc/service
ADD ./nginx_reload.sh /nginx_reload.sh
ADD ./certctl.py /certctl.py
ADD ./nginx.conf /etc/nginx/nginx.conf

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

RUN find /etc/service -name run | xargs chmod +x \
&& mkdir -p \
    /etc/container_environment \
    /var/www \
    /etc/nginx/ssl \
    /etc/nginx/sites-enabled \
    /etc/my_init.d \
    /var/cache/nginx \
    /var/spool/nginx \
&& chmod +x \
    /sbin/my_init \
    /nginx_reload.sh \
    /certctl.py \
    /etc/runit/2 \
&& chmod 444 \
    /etc/nginx/nginx.conf

VOLUME /var/cache/nginx

CMD ["/sbin/my_init"]
