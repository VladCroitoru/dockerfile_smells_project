FROM opensuse:13.2
MAINTAINER Erik Henrikson <erik.henrikson@emc.com>
 
#
# Install prerequisite software
#

RUN zypper --non-interactive install keepalived wget openssh-fips telnet aaa_base arping2 python python-base mozilla-nss sudo ipcalc java-1_7_0-openjdk

# Need to get sipcalc - using "unstable" one from opensuse
ADD sipcalc-1.1.6-5.1.x86_64.rpm /
RUN rpm -Uvh --nodeps sipcalc-1.1.6-5.1.x86_64.rpm && \
 	rm -f sipcalc-1.1.6-5.1.x86_64.rpm

# Create users/groups
RUN groupadd storageos && useradd -d /opt/storageos -g storageos storageos
RUN groupadd svcuser && useradd -g svcuser svcuser

#
# Download, compile, and install nginx
#
RUN zypper --non-interactive install --no-recommends patch gcc-c++ pcre-devel libopenssl-devel tar make && \
	wget http://nginx.org/download/nginx-1.6.2.tar.gz && \
 	wget --no-check-certificate https://github.com/yaoweibin/nginx_upstream_check_module/archive/v0.3.0.tar.gz && \
	wget --no-check-certificate https://github.com/openresty/headers-more-nginx-module/archive/v0.25.tar.gz && \
	tar xvzf nginx-1.6.2.tar.gz && tar xvzf v0.3.0.tar.gz && tar xvzf v0.25.tar.gz && \
	cd nginx-1.6.2 && patch -p1 < ../nginx_upstream_check_module-0.3.0/check_1.5.12+.patch && ./configure --add-module=../nginx_upstream_check_module-0.3.0 --add-module=../headers-more-nginx-module-0.25 --with-http_ssl_module --prefix=/usr --conf-path=/etc/nginx/nginx.conf && make && make install && cd .. && \
	rm -f nginx-1.6.2.tar.gz v0.3.0.tar.gz v0.25.tar.gz && \
	rm -rf nginx-1.6.2 nginx_upstream_check_module-0.3.0 headers-more-nginx-module-0.25 && \
	zypper --non-interactive remove apache2-prefork apache2 apache2-utils patch gcc-c++ pcre-devel libopenssl-devel tar make

CMD ["/sbin/init"]

