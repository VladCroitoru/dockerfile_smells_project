# "adopted" by jamitupya@gmail.com for use in a reverse proxy template; 
# and yes, it is cobbled together in my 2nd attempt at docker so comments welcome
# Updates to come: 
# + make the compile's into a series of scripts and not just in the dockerfile
# + remove legacy unused dependencies via yum
# + add /logs/ documentation for logrotate in image onto local host filesystem
# + add /ssl/ documentation for including a volume that hosts your SSL Certs
#
# "ported" by Adam Miller <maxamillion@fedoraproject.org> from
#   https://github.com/fedora-cloud/Fedora-Dockerfiles
#
# Originally written for Fedora-Dockerfiles by
#   scollier <scollier@redhat.com>

FROM centos:centos7
#MAINTAINER The CentOS Project <cloud-ops@centos.org>
MAINTAINER Jamitupya <jamitupya@gmail.com>

ENV NPS_VERSION=1.11.33.2
ENV OPENSSL_VERSION=1.0.2h
ENV OPENSSL_OLD=
ENV NGINX_VERSION=1.11.2
ENV NGINX_CONF_GIT_REPO=https://bitbucket.org/gahnget/template/
ENV NGINX_CONF_GIT_BRANCH=master
ENV GEOIP_CITY_NAME=GeoLiteCityv6.dat
ENV GEOIP_COUNTRY_NAME=GeoLiteCountry.dat
ENV GEOIP2_CITY_NAME=GeoLite2-City.mmdb
ENV GEOIP2_COUNTRY_NAME=GeoLite2-Country.mmdb

# UPDATE THESE TO YOUR OWN. DO NOT USE THESE, both must be in base64 format
ENV NGINX_CONF_GIT_SSH_PUB=c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFCQVFEcFdYdVFNRC8zWUd2L05ja2dvQXdOT2JBdGdyMmFaTE5CWGtYMkNzZm1HblowRURLRXhiMWNQWnF0dE00TzBHZ3RDd3hTeU5TK3VrVndUdG9aTmRXMnl6M3A1a0VZa01PWTBBeWJqODJNeVRSZ1FpMTk3Rkg5TDdwZTZLQVFiOUcyQm5UZkxIQmg3Y29URnpzaDdrdlJObW9ESmhTUkZXVGNrZjlKU0FWSU0zRDZUZmJOSG9FUjhod20vSWs3bFlsRlFxNThwcE5aMTAwQ0hYQklkQS9zbnVPcEJpdmh0amV4Q0paRHJ5NTVZRlFkc2lQTkFVT0YxbStDN3EzYUFvNjNQNTVVa2NJSEZ3V05XTmNUbTc5SGg3TFNiaEtXY3dkdUlOYjA3NHFjbmpmRmV5Um81U2MvNjhDWTlwS1dLRmVaMG95MUN6RS9uVU5NUG5HSmxScXogcm9vdEBjZW50b3MtYnVpbGQtZG9ja2VyLmVwaWNpZ3VhbmEuY29t
ENV NGINX_CONF_GIT_SSH_PVT=LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQ0KTUlJRXBRSUJBQUtDQVFFQTZWbDdrREEvOTJCci96WEpJS0FNRFRtd0xZSzltbVN6UVY1Rjlnckg1aHAyZEJBeQ0KaE1XOVhEMmFyYlRPRHRCb0xRc01Vc2pVdnJwRmNFN2FHVFhWdHNzOTZlWkJHSkREbU5BTW00L05qTWswWUVJdA0KZmV4Ui9TKzZYdWlnRUcvUnRnWjAzeXh3WWUzS0V4YzdJZTVMMFRacUF5WVVrUlZrM0pIL1NVZ0ZTRE53K2szMg0KelI2QkVmSWNKdnlKTzVXSlJVS3VmS2FUV2RkTkFoMXdTSFFQN0o3anFRWXI0Ylkzc1FpV1E2OHVlV0JVSGJJag0KelFGRGhkWnZndTZ0MmdLT3R6K2VWSkhDQnhjRmpWalhFNXUvUjRleTBtNFNsbk1IYmlEVzlPK0tuSjQzeFhzaw0KYU9VblArdkFtUGFTbGloWG1kS010UXN4UDUxRFRENXhpWlVhc3dJREFRQUJBb0lCQUY5ZXZCcU5MY2VMOS9laA0KWXVkYm9qRlJqNGk2TTRYRGZHUE9CT2Z2TmczOGFNYzh5M2pxWEY4enFtRXVVVDFLdmhrU3QrR3B4UkdDamRpOQ0KMFhPV1JoZGtiNVNHRDdyYmg2V1ArbWNsMmN1ZGZET1BPSXFMcUdMRE8vZUlPY3NkK0diZHNxeDN2Q0s2RGVuSg0KaDloeFRUbGZkT3AraU05WElCYnA4SjFodXc3cmQ0Z1crdkdDNjltaStvRzZZWVFETElKREg4UnZqdlF2NDN4dw0KRzVTbXM4Z2ZKYWNzUXhRZTJIc2kwT0FReHF4dWlpVERLd25EYTI2SklCTUp0eTFtaEpvUzNkVDl1dnNDTVpmNA0KT2NXR0hQbG4yclVhMTAxbXZYQXcrVFpIWWowcnZvalVwYTJKZS9WWngzMVlvM2M0Lyt2SHRLYXRyS3ZpMVdrRw0KQzg0djkya0NnWUVBOXcxc3NWWmErUCt4YVhuSFlvSTlmZkxoZ2pYbmQzQ0NxY3lQaytITEl0YzNoWlZodkFlZg0KWFBIZm9PZGd1OTUzbVF2bUNEaG1tckxhRXl6dGE4ZGJOanE1eVhkM0VVVWsxSjJSbFZ2TkF1cHZxdXp3Rlc0UQ0KY0l3UlZMYTJEbWlzeExuNHpOZG9NNzhzK1BQOFJqTTdwY1J2RDhYdnNwUUVsQmVwVkE1ekQ4MENnWUVBOGMwQw0KbEVmWXphSzZFL1RmR2hxdWJpY1Q0V1dZWmFhU2hxcklKd25jejJQT0s4cUw5U0Q2aDVPbXFPUTFpSlhva0JFcA0KM0NxaWdSOVRrOUR5T05Ic1RicDlYVWZQTWdIaWVRUzJFS2xLYW5ETEw4OHdaWUZUMzByQUhwekROSDhma1V4OQ0KVE9RR241NFc2K1VxVHRXaFhFSExXeFBPTUk5eHlxOVJFUmVWVkg4Q2dZRUFrdUNkVlZWRTRyS0psRzY5Tm5pOQ0KL0VwUS9ldjBRQk5ZNjRCZGdBc0dqU0VzdGpPWWxvUmxuNG1CYlpVQjhzK1JoU0VJMHF4TmUvMkhIMDFmbmVzNA0KOUNXMzNPbzBsTVRwMzZvS0txVVlYbnBvaDFNMGJWa3hWdWcvU1lFUy9jQUhyekh0bEVNZ2hWdE1ibm9INnVoOA0KdHRIeFFZeHBORjlCMVpXM3F1eW9SYVVDZ1lFQXErNmlUdDFuZzVDWnoyYm0zS0RzTnRjQ2c5ckJxa1h2R21LRg0KUDN6N3pWdWlWZkVINDUwM2h2K3VHWmxybDF0QXFuQUoyOHRWRVlzODJuWlFSYWErNStZYkRpRHBheDE3ODZFdA0KOUZycjF4T3M1cW5rTjhqbDRuZzhjNGYwSlhmZThtbjVEcHQxT2pvbkFrVkkrQlZmVDBKWlhzR09jMmtMK0pzQQ0KZ2E3TE4vRUNnWUVBeGxOaDBCVURLZ2huV2JUMk5uTDgzRFRMT3NNeGF6aHZXSTljdVI2WUhZT1dPcTBXNWFRdA0KTVFWMXl5WFlJR3dqZWtCbW9SbTl5NWhZSUxGdnZ3RkJ0ellVUmZYUDkrcm82RVd5R2xqWXhDRHp2QmhSYUxlUA0KRHJySjJUMW9SbUVOZGtNdmhyVHFrek0zcHZLN1YwZXJZL0kvK1ArOWVkaWdBUksvMXNaNjE1ST0NCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t

# Update to latests builds
RUN yum -y install epel-release tar ; yum clean all
RUN yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm ; yum clean all
RUN yum -y install yum-utils ; yum-config-manager --save --setopt=epel.skip_if_unavailable=true ; yum -y update --exclude=kernel* ; yum clean all

# Install compile tools + prerequisites
RUN yum -y --enablerepo=remi,remi-php70 groupinstall 'Development Tools'
RUN yum -y --enablerepo=remi,remi-php70 install git pcre-devel libxml2 libxml2-devel libcurl-devel gcc gcc-c++ doc-base gd wget bison libtool zlib-devel libgssapi-devel libunwind automake autoconf libatomic unzip bzip2-devel libnet-devel python2 python2-devel python-pip jansson-devel libxml2 libxslt libcap-ng-devel libnet-devel readline-devel libpcap-devel libcap-ng-devel libyaml-devel GeoIP-devel lm_sensors-libs net-snmp-libs net-snap gd-devel libnetfilter_queue-devel libnl-devel popt-devel lsof ipvsadm openssh nss-devel ncurses-devel glib2-devel file-devel geoip-devel luajit-devel luajit lua-devel ; yum clean all

# setup source ssh private and public keys
# Create known_hosts
RUN mkdir ~/.ssh
RUN touch ~/.ssh/known_hosts

# Add github (or your git server) fingerprint to known hosts
RUN ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
RUN touch ~/.ssh/id_rsa.pub && touch ~/.ssh/id_rsa 
RUN echo ${NGINX_CONF_GIT_SSH_PUB} | base64 --decode >> ~/.ssh/id_rsa.pub && chmod 700 ~/.ssh/id_rsa.pub
RUN echo ${NGINX_CONF_GIT_SSH_PVT} | base64 --decode >> ~/.ssh/id_rsa && chmod 700 ~/.ssh/id_rsa
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /etc/ssh/ssh_config
#RUN ssh-agent /bin/bash
RUN echo "IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config
#RUN ssh-add ~/.ssh/id_rsa ; ssh-add -l
#RUN ssh -T git@bitbucket.com

# setup libmaxminddb
RUN cd /usr/src && git clone --recursive https://github.com/maxmind/libmaxminddb && cd libmaxminddb && ./bootstrap ; ./configure ; make ; make check ; make install
RUN echo /usr/local/lib >> /etc/ld.so.conf.d/local.conf
RUN ldconfig ; rm -rf /usr/src/libmaxminddb

# setup autoupdate of geoip databases using temp account details; can be overwritten by including an ADD of GeoIP.conf to the path /usr/local/etc/
RUN cd /usr/src/ && git clone https://github.com/maxmind/geoipupdate && cd geoipupdate && ./bootstrap ; ./configure ; make ; make install ; mkdir /usr/local/share/GeoIP
ADD GeoIP.conf /usr/local/etc/GeoIP.conf
RUN /usr/local/bin/geoipupdate
RUN ln -s /usr/local/share/GeoIP/${GEOIP_CITY_NAME:-GeoLiteCity.dat} /usr/local/share/GeoIP/geoip_city.dat ; ln -s /usr/local/share/GeoIP/${GEOIP_COUNTRY_NAME:-GeoLiteCountry.dat} /usr/local/share/GeoIP/geoip_country.dat
RUN ln -s /usr/local/share/GeoIP/${GEOIP2_CITY_NAME:-GeoLite2-City.mmdb} /usr/local/share/GeoIP/geoip2_city.mmdb ; ln -s /usr/local/share/GeoIP/${GEOIP2_COUNTRY_NAME:-GeoLite2-Country.mmdb} /usr/local/share/GeoIP/geoip2_country.mmdb

# compile brotli + prerequisites
RUN cd /usr/src/ ; git clone https://github.com/bagder/libbrotli libbrotli
RUN cd /usr/src/libbrotli ; sh autogen.sh ; sh configure ; make ; make install ; rm -rf /usr/src/libbrotli 

# compile pagespeed prerequisites
RUN cd /usr/src && git clone https://github.com/gperftools/gperftools gperftools && cd /usr/src/gperftools ; ./configure --enable-frame-pointers ; make ; make install ; ldconfig ; cd /usr/src/ && rm -rf /usr/src/gperftools*

# get openssl sources
RUN cd /usr/src/ && wget https://www.openssl.org/source/openssl-${OPENSSL_VERSION:-1.0.2g}.tar.gz && tar -xvzf openssl-${OPENSSL_VERSION:-1.0.2g}.tar.gz ; cd /usr/src/ && rm -rf *.tar.gz

# get nginx sources
RUN cd /usr/src && wget http://nginx.org/download/nginx-${NGINX_VERSION:-1.9.12}.tar.gz && tar -xvzf nginx-${NGINX_VERSION:-1.9.12}.tar.gz ; rm -rf nginx-${NGINX_VERSION:-1.9.12}.tar.gz

# get nginx module prerequisites
RUN mkdir /usr/src/nginx-modules/ && cd /usr/src/nginx-modules/ && git clone https://github.com/simpl/ngx_devel_kit && git clone https://github.com/kyprizel/testcookie-nginx-module && git clone https://github.com/Lax/ngx_http_accounting_module.git && git clone https://github.com/openresty/headers-more-nginx-module && git clone https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng && git clone https://github.com/openresty/lua-nginx-module && git clone https://github.com/openresty/lua-upstream-nginx-module && git clone https://github.com/vozlt/nginx-module-vts && git clone https://github.com/google/ngx_brotli && git clone https://github.com/yzprofile/ngx_http_dyups_module && git clone https://github.com/cubicdaiya/ngx_dynamic_upstream && git clone https://github.com/leev/ngx_http_geoip2_module && git clone https://github.com/nbs-system/naxsi && cd naxsi && git checkout http2
RUN cd /usr/src/nginx-modules && wget https://github.com/pagespeed/ngx_pagespeed/archive/release-${NPS_VERSION:-1.10.33.6}-beta.zip && unzip release-${NPS_VERSION:-1.10.33.6}-beta.zip && cd ngx_pagespeed-release-${NPS_VERSION:-1.10.33.6}-beta && wget https://dl.google.com/dl/page-speed/psol/${NPS_VERSION:-1.10.33.6}.tar.gz && tar -xzvf ${NPS_VERSION:-1.10.33.6}.tar.gz
RUN ls -la /usr/src/nginx-modules/

# compile nginx prerequisites
RUN export LUAJIT_LIB=/usr/local/lib/libluajit-5.1.so && export LUAJIT_INC=/usr/local/include/luajit-2.0 && LUAJIT_LIB_PATH=/usr/local/lib/libluajit-5.1.so && LUAJIT_INC_PATH=/usr/local/include/luajit-2.0/
RUN cd /usr/src/nginx-${NGINX_VERSION:-1.9.12} && ./configure --with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2' \
--with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-rpath,/usr/local/include,-rpath,/usr/local/lib' \
--sbin-path=/usr/sbin/nginx \
--user=nginx \
--group=nginx \
--prefix=/etc/nginx \
--conf-path=/etc/nginx/nginx.conf \
--error-log-path=/logs/nginx/error.log \
--http-log-path=/logs/nginx/access.log \
--http-client-body-temp-path=/tmp/client_body \
--http-proxy-temp-path=/tmp/proxy \
--http-fastcgi-temp-path=/tmp/fastcgi \
--pid-path=/var/run/nginx.pid \
--lock-path=/var/lock/subsys/nginx \
--with-http_ssl_module \
--with-pcre-jit \
--with-http_secure_link_module \
--with-openssl-opt=enable-tlsext \
--with-http_v2_module \
--with-http_ssl_module \
--with-openssl=/usr/src/openssl-${OPENSSL_VERSION:-1.0.2g} \
--with-file-aio \
--with-http_realip_module \
--with-http_addition_module \
--with-http_sub_module \
--with-ipv6 \
--with-http_flv_module \
--with-http_geoip_module=dynamic \
--with-http_gzip_static_module \
--with-http_stub_status_module \
--with-threads \
--with-http_image_filter_module=dynamic \
--with-mail=dynamic \
--with-stream=dynamic \
--add-dynamic-module=/usr/src/nginx-modules/ngx_devel_kit \
--add-dynamic-module=/usr/src/nginx-modules/lua-nginx-module \
--add-dynamic-module=/usr/src/nginx-modules/headers-more-nginx-module \
--add-dynamic-module=/usr/src/nginx-modules/ngx_pagespeed-release-${NPS_VERSION:-1.10.33.6}-beta \
--add-dynamic-module=/usr/src/nginx-modules/lua-upstream-nginx-module \
#--add-dynamic-module=/usr/src/nginx-modules/ngx_brotli \
--add-dynamic-module=/usr/src/nginx-modules/naxsi/naxsi_src \
--add-dynamic-module=/usr/src/nginx-modules/testcookie-nginx-module \
--add-dynamic-module=/usr/src/nginx-modules/ngx_http_dyups_module \
--add-dynamic-module=/usr/src/nginx-modules/ngx_dynamic_upstream \
--add-dynamic-module=/usr/src/nginx-modules/ngx_http_geoip2_module \
--add-dynamic-module=/usr/src/nginx-modules/ngx_http_accounting_module \
#--add-module=/usr/src/nginx-modules/nginx-sticky-module-ng \
--add-dynamic-module=/usr/src/nginx-modules/nginx-module-vts
#--add-module=/usr/src/nginx-modules/nginx-module-vts
RUN cd /usr/src/nginx-${NGINX_VERSION:-1.9.12} && make -j2 && make install
RUN cd /usr/src/ && ls -la /etc/nginx/modules ; rm -rf /usr/src/nginx-${NGINX_VERSION:-1.9.12} ; rm -rf /usr/src/nginx-modules ; rm -rf /usr/src/openssl-${OPENSSL_VERSION:-1.0.2g}

#RUN yum -y install nginx ; yum clean all
ADD nginx.conf /etc/nginx/nginx.conf

# pull git repo for conf.d directory
RUN git clone ${NGINX_CONF_GIT_REPO} /etc/nginx/conf.d
RUN cd /etc/nginx/conf.d/ ; ls -la 

# setup final paths and init.d for nginx
RUN mkdir /var/lib/nginx && mkdir /etc/nginx/default && mkdir /logs && mkdir /logs/nginx && mkdir /var/lib/nginx/tmp && mkdir /tmp/nginx_cache && id -u nginx &>/dev/null || useradd -s /usr/sbin/nologin -r nginx && chown -R nginx:nginx /etc/nginx && chown -R nginx:nginx /var/lib/nginx && chown -R nginx:nginx /logs/nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN curl https://git.centos.org/sources/httpd/c7/acf5cccf4afaecf3afeb18c50ae59fd5c6504910 \
    | tar -xz -C /etc/nginx/default \
    --strip-components=1
RUN sed -i -e 's/Apache/nginx/g' -e '/apache_pb.gif/d' \ 
    /etc/nginx/default/index.html
RUN yum -y groupremove 'Development Tools' ; yum -y remove *-devel ; yum -y update ; yum clean all

EXPOSE 80
EXPOSE 443

CMD [ "/usr/sbin/nginx" ]