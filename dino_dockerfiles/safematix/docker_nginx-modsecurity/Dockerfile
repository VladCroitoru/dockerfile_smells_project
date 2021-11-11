FROM ubuntu:16.04
MAINTAINER Robert Ressl <r.ressl@safematix.com>

ENV DEBIAN_FRONTEND noninteractive
ENV UBUNTU_VERSION xenial
ENV NGINX_VERSION 1.13.6
ENV MODSECURITY_VERSION v3

# install build tools and libraries
RUN apt-get update \
 && apt-get install -y \
            dpkg-dev apache2-dev libpcre3-dev libxml2-dev \
            g++ flex bison doxygen libyajl-dev libgeoip-dev libtool dh-autoreconf libcurl4-gnutls-dev libxml2 libpcre++-dev pkgconf zlib1g-dev \
            git curl \
            supervisor

# download modsecurity
RUN cd /usr/src/ \
 && git clone https://github.com/SpiderLabs/ModSecurity \
 && cd ModSecurity/ \
 && git checkout -b ${MODSECURITY_VERSION}/master origin/${MODSECURITY_VERSION}/master \
 && git submodule init \
 && git submodule update

# build modsecurity
RUN cd /usr/src/ModSecurity \
 && ./build.sh \
 && ./configure \
 && make -j 16 \
 && make install

# download ModSecurity-nginx
RUN cd /usr/src \
 && git clone https://github.com/SpiderLabs/ModSecurity-nginx.git

# download nginx
RUN cd /usr/src \
 && echo "deb-src http://nginx.org/packages/mainline/ubuntu/ ${UBUNTU_VERSION} nginx" > /etc/apt/sources.list.d/nginx.list \
 && curl -O http://nginx.org/keys/nginx_signing.key \
 && apt-key add nginx_signing.key \
 && apt-get update \
 && apt-get source nginx \
 && apt-get -qy build-dep nginx

# build nginx with ModSecurity-nginx
RUN cd /usr/src/nginx-* \
 && sed -i -e 's%dh_shlibdeps%dh_shlibdeps -a --dpkg-shlibdeps-params=--ignore-missing-info%' debian/rules \
 && sed -i -e 's%\./configure%./configure --add-module=/usr/src/ModSecurity-nginx --with-http_stub_status_module%' debian/rules \
 && dpkg-buildpackage -b \
 && dpkg -i /usr/src/nginx_*.deb

# download owasp rules
RUN cd /usr/src \
 && git clone https://github.com/SpiderLabs/owasp-modsecurity-crs

# configure nginx for modsecurity
RUN mkdir /etc/nginx/modsecurity \
 && chown nginx:nginx /etc/nginx/modsecurity \
 && cd /etc/nginx \
 && sed -i -e '/keepalive_timeout/a\' -e '    modsecurity on;' nginx.conf \
 && sed -i -e '/modsecurity/a\' -e '    modsecurity_rules_file /etc/nginx/modsecurity/modsec_includes.conf;' nginx.conf

# copy ModSecurity config and owasp rules
RUN cp -a /usr/src/ModSecurity/modsecurity.conf-recommended /etc/nginx/modsecurity/modsecurity.conf \
 && cp -a /usr/src/owasp-modsecurity-crs /etc/nginx/modsecurity/ \
 && cd /etc/nginx/modsecurity/owasp-modsecurity-crs/ \
 && mv crs-setup.conf.example crs-setup.conf \
 && cd /etc/nginx/modsecurity/owasp-modsecurity-crs/rules/ \
 && mv REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf.example REQUEST-900-EXCLUSION-RULES-BEFORE-CRS.conf \
 && mv RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf.example RESPONSE-999-EXCLUSION-RULES-AFTER-CRS.conf

# tune nginx
RUN sed -i 's^worker_processes  1;^worker_processes auto;^g' /etc/nginx/nginx.conf \
 && sed -i -e '/worker_processes/a\' -e 'worker_cpu_affinity auto;' /etc/nginx/nginx.conf \
 && sed -i 's^worker_connections  1024;^worker_connections  4096;^g' /etc/nginx/nginx.conf \
 && sed -i -e '/worker_connections/a\' -e '    multi_accept on;' /etc/nginx/nginx.conf

# security nginx
RUN sed -i -e '/modsecurity_rules_file/a\' -e '    server_tokens off;' /etc/nginx/nginx.conf

# cleanup not needed files
RUN apt-get -y purge git dpkg-dev apache2-dev libpcre3-dev libxml2-dev \
 && apt -y autoremove \
 && apt -y autoclean

RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* \
 && rm -rf /usr/src/*

COPY files/root /

VOLUME /etc/nginx

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/entrypoint.sh"]
