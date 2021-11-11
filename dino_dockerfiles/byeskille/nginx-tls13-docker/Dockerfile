# To build and run this container locally, try a command like:
#
#        docker build -t nginx .
#        docker run --cap-drop=all --name nginx -d -p 80:8080 nginx
# **deprecated:** This repo is not updated at all anymore. Ubuntu 18.04 with nginx from the official repos now support TLS 1.3 out of the box. And that is more recommended even for experimentation.

FROM ubuntu:16.04
MAINTAINER Øyvind Bye Skille <oyvind@byeskille.no>

# Nginx Version (See: https://nginx.org/en/CHANGES)
ENV NGXVERSION 1.15.11
ENV NGXSIGKEY B0F4253373F8F6F510D42178520A9993A1C052F8

# OpenSSL Version (See: https://www.openssl.org/source/)
ENV OSSLVER 1.1.1-pre9-dev
ENV OSSLSIGKEY 0E604491

# Build as root (we drop privileges later when actually running the container)
USER root
WORKDIR /root

## not in

# Mod 'www-data' user
RUN usermod www-data  --home /etc/nginx --shell /sbin/nologin

# Update and upgrade
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoclean && \
    apt-get autoremove

#Install deps
RUN apt-get install -y \
        libpcre3 \
        libpcre3-dev \
        zlib1g-dev &&\
    apt-get autoclean

# Get sources into container, verify, compile and install - purge after
RUN apt-get install -y wget git gcc make && \
    wget https://nginx.org/download/nginx-$NGXVERSION.tar.gz && \
    git clone -b master --single-branch https://github.com/openssl/openssl && \
    wget https://nginx.org/download/nginx-$NGXVERSION.tar.gz.asc && \
    gpg --keyserver keyserver.ubuntu.com --recv-keys $NGXSIGKEY && \
    out=$(gpg --status-fd 1 --verify "nginx-$NGXVERSION.tar.gz.asc" 2>/dev/null) && \
    if echo "$out" | grep -qs "\[GNUPG:\] GOODSIG" && echo "$out" | grep -qs "\[GNUPG:\] VALIDSIG"; then echo "Good signature on nginx source."; else echo "GPG VERIFICATION OF NGINX SOURCE FAILED!" && echo "EXITING!" && exit 100; fi && \
    tar -xzvf nginx-$NGXVERSION.tar.gz && \
    rm -v nginx-$NGXVERSION.tar.gz && \
    cd "/root/nginx-$NGXVERSION/" && \
    ./configure --prefix=/etc/nginx --sbin-path=/usr/sbin/nginx --modules-path=/usr/lib/nginx/modules --conf-path=/etc/nginx/nginx.conf --error-log-path=/var/log/nginx/error.log --http-log-path=/var/log/nginx/access.log --pid-path=/var/run/nginx.pid --lock-path=/var/run/nginx.lock --http-client-body-temp-path=/var/cache/nginx/client_temp --http-proxy-temp-path=/var/cache/nginx/proxy_temp --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp --http-scgi-temp-path=/var/cache/nginx/scgi_temp --user=nginx --group=nginx --with-compat --with-file-aio --with-threads --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --with-http_v2_module --with-mail --with-mail_ssl_module --with-stream --with-stream_realip_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fPIC' --with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie' --with-openssl="$HOME/openssl" --with-openssl-opt=enable-tls1_3 && \
    make && \
    make install && \
    apt-get purge -y --auto-remove wget git gcc make && \
    rm -R "/root/nginx-$NGXVERSION" && \
    rm -R "/root/openssl"



# Make sure the permissions are set correctly on our webroot, logdir and pidfile so that we can run the webserver as non-root.
RUN chown -R www-data:www-data /etc/nginx && \
    chown -R www-data:www-data /var/log/nginx && \
    mkdir -p /var/cache/nginx/ && \
    chown -R www-data:www-data /var/cache/nginx/ && \
    touch /run/nginx.pid && \
    chown -R www-data:www-data /run/nginx.pid

# Configure nginx to listen on 8080 instead of 80 (we can't bind to <1024 as non-root)
#RUN perl -pi -e 's,80;,8080;,' /etc/nginx/nginx.conf

# Print built version
RUN nginx -V

# Launch Nginx in container as non-root
USER www-data
WORKDIR /etc/nginx

# Launch command
CMD ["nginx", "-g", "daemon off;"]
