FROM alpine:3.4

MAINTAINER kpavlov "mail@konstantinpavlov.net"

# Set working dir
ENV WORKING_DIRECTORY=/opt/build
RUN mkdir -p $WORKING_DIRECTORY
WORKDIR $WORKING_DIRECTORY

VOLUME /etc/nginx/external
VOLUME /usr/share/nginx/html

# ENV build variables
ENV LANG C.UTF-8
ENV LC_ALL=C
ENV NGINX_VERSION=1.10.1
ENV MODSEC_VERSION=2.9.1
ENV NGINX_CONFIG_BASE="\
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
  --with-http_image_filter_module=dynamic \
  --with-http_geoip_module=dynamic \
  --with-threads \
  --with-stream \
  --with-stream_ssl_module \
  --with-http_slice_module \
  --with-mail \
  --with-mail_ssl_module \
  --with-file-aio \
  --with-http_v2_module \
  --with-ipv6 \
  "
ENV NGINX_CONFIG_MODSECURITY=" --add-module=$WORKING_DIRECTORY/ModSecurity/nginx/modsecurity "

# 1 Install required dependencies
# 2 Compile Mod Security
# 3 Get Mod security configs
# 4 Compile Nginx
# 5 Configure Nginx
# 6 Clean solution
RUN \
    addgroup -S nginx && \
    adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx && \
    apk update && \
    echo "#### Install required dependencies ####" && \
    apk add --no-cache \
      apache2-dev \
      autoconf \
      automake \
      bash \
      build-base \
      curl \
      gd-dev \
      geoip-dev \
      git \
      libtool \
      libxml2 \
      libxml2-dev \
      linux-headers \
      m4 \
      openssl-dev \
      pcre-dev \
      unzip \
      wget \
      zlib-dev && \
    \
    echo "#### Compile Mod Security ####" && \
    wget https://github.com/SpiderLabs/ModSecurity/releases/download/v${MODSEC_VERSION}/modsecurity-${MODSEC_VERSION}.tar.gz && \
    tar -xvzf modsecurity-${MODSEC_VERSION}.tar.gz && \
    mv modsecurity-${MODSEC_VERSION} ModSecurity && \
    cd ModSecurity && \
    ./autogen.sh && \
    ./configure --enable-standalone-module --disable-mlogc && \
    make && \
    make install && \
    cd .. && \
    wget https://raw.githubusercontent.com/SpiderLabs/ModSecurity/master/modsecurity.conf-recommended && \
    mkdir -p /etc/nginx/modsecurity/rules && \
    cat modsecurity.conf-recommended  > /etc/nginx/modsecurity/modsecurity.conf && \
    \
    echo "#### Get Mod security configs ####" && \
    wget https://github.com/SpiderLabs/owasp-modsecurity-crs/tarball/master -O owasp-modsecurity-crs.tar.gz && \
    tar -xvzf owasp-modsecurity-crs.tar.gz && \
    CRS_DIR=$(find . -type d -name SpiderLabs-owasp-modsecurity-crs*) && \
    cp -v ${CRS_DIR}/modsecurity_crs_10_setup.conf.example /etc/nginx/modsecurity/modsecurity_crs_10_setup.conf && \
    cp -v ${CRS_DIR}/base_rules/modsecurity_*.conf /etc/nginx/modsecurity/rules/ && \
    cp -v ${CRS_DIR}/base_rules/*.data /etc/nginx/modsecurity/rules/ && \
    cp ModSecurity/unicode.mapping /etc/nginx/modsecurity/unicode.mapping && \
    echo 'Include /etc/nginx/modsecurity/modsecurity_crs_10_setup.conf' >> /etc/nginx/modsecurity/modsecurity.conf && \
    echo 'Include /etc/nginx/modsecurity/rules/*.conf' >> /etc/nginx/modsecurity/modsecurity.conf && \
    echo 'Include /etc/nginx/modsecurity/modsecurity_extra.conf' >> /etc/nginx/modsecurity/modsecurity_extra.conf && \
    echo "#### Tune Mod security configs ####" && \
    echo 'SecDefaultAction "log,deny,phase:1"' >> /etc/nginx/modsecurity/modsecurity.conf && \
    sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/g' /etc/nginx/modsecurity/modsecurity.conf && \
    sed -i 's/SecStatusEngine On/SecStatusEngine Off/g' /etc/nginx/modsecurity/modsecurity.conf && \
    sed -i 's/SecAuditLogType Serial/SecAuditLogType Concurrent/g' /etc/nginx/modsecurity/modsecurity.conf && \
    sed -i 's/SecAuditLog(.*)/#SecAuditLog\1/g' /etc/nginx/modsecurity/modsecurity.conf && \
    sed -i 's/#SecAuditLogStorageDir.*/SecAuditLogStorageDir \/var\/log\/nginx\/modsecurity_audit\//g' /etc/nginx/modsecurity/modsecurity.conf && \
    touch /etc/nginx/modsecurity/modsecurity_extra.conf && \
    \
    echo "#### Compile Nginx ####" && \
    wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \
    tar -xvzf nginx-${NGINX_VERSION}.tar.gz && \
    cd nginx-${NGINX_VERSION}/ && \
    ./configure $NGINX_CONFIG_BASE $NGINX_CONFIG_MODSECURITY && \
    make && \
    make install && \
    rm /etc/nginx/nginx.conf && \
    mkdir -p /usr/share/nginx/html/ && \
    cp -vR /etc/nginx/html /usr/share/nginx/ && \
    #rm -rf /etc/nginx/html/ && \
    cd .. && \
    echo "#### Configure Nginx ####" && \
    # forward request and error logs to docker log collector
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    echo "#### Clean solution ####" && \
    apk del \
      *.dev \
      autoconf \
      automake \
      build-base \
      git \
      unzip \
      linux-headers && \
    rm -rf $WORKING_DIRECTORY \
      modsecurity.conf-recommended \
      nginx-${NGINX_VERSION}.tar.gz \
      nginx-${NGINX_VERSION} \
      owasp-modsecurity-crs.tar.gz


# Set workdir
WORKDIR /etc/nginx

# Check Nginx installation
RUN nginx -V

# Enable basic configurations and import of external configurations
RUN apk add openssl && \
    rm -rf /etc/nginx/conf.d/* 
COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY basic.conf /etc/nginx/conf.d/basic.conf
COPY ssl.conf /etc/nginx/conf.d/ssl.conf
COPY security.conf /etc/nginx/conf.d/security.conf
COPY entrypoint.sh /opt/entrypoint.sh
RUN chmod a+x /opt/entrypoint.sh
ENTRYPOINT ["/opt/entrypoint.sh"]

VOLUME /var/log/nginx

EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]