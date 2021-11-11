# Based on the Dockerfile from https://github.com/g17/nginx-ldap
FROM debian:stretch

MAINTAINER Michael Klein <mwklein@happycynic.com>

ENV NGINX_VERSION release-1.21.1

# Use stretch-backports for openssl >= 1.0.2
# This is required by nginx-auth-ldap when ssl_check_cert is turned on.
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
	&& echo 'deb http://ftp.debian.org/debian/ stretch-backports main' > /etc/apt/sources.list.d/backports.list \
	&& apt-get update \
	&& apt-get install -t stretch-backports -y \
		ca-certificates \
		git \
		gcc \
		make \
		libpcre3-dev \
		zlib1g-dev \
		libldap2-dev \
		libssl-dev \
		wget \
		cron \
		certbot 

# See http://wiki.nginx.org/InstallOptions
RUN mkdir /var/log/nginx \
	&& mkdir /etc/nginx \
	&& cd ~ \
	&& git clone https://github.com/kvspb/nginx-auth-ldap.git \
	&& git clone https://github.com/nginx/nginx.git \
	&& cd ~/nginx \
	&& git checkout tags/${NGINX_VERSION} \
	&& ./auto/configure \
		--add-module=/root/nginx-auth-ldap \
		--with-http_ssl_module \
		--with-debug \
		--conf-path=/etc/nginx/nginx.conf \ 
		--sbin-path=/usr/sbin/nginx \ 
		--pid-path=/var/log/nginx/nginx.pid \ 
		--error-log-path=/var/log/nginx/error.log \ 
		--http-log-path=/var/log/nginx/access.log \
        --with-stream \
        --with-stream_ssl_module \
        --with-debug \
        --with-file-aio \
        --with-threads \
        --with-http_gunzip_module \
        --with-http_gzip_static_module \
        --with-http_v2_module \
        --with-http_auth_request_module \
	&& make install \
	&& cd .. \
	&& rm -rf nginx-auth-ldap \
	&& rm -rf nginx \
	&& wget -O /tmp/dockerize.tar.gz https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz \
	&& tar -C /usr/local/bin -xzvf /tmp/dockerize.tar.gz \
	&& rm -rf /tmp/dockerize.tar.gz

# Add letsencrypt renewal to cron (kills container after renew is complete)
RUN echo '30 2 * * 1 /usr/bin/letsencrypt renew >> /var/log/le-renew.log' >> mycron \
	&& echo '35 2 * * 1 kill $(ps aux | grep '[d]ockerize' | awk '{print $2}')' >> mycron \
	&& crontab mycron \
	&& rm mycron

EXPOSE 80 443

RUN mkdir -p /var/www/html

COPY run.sh /run.sh

VOLUME ["/etc/nginx", "/etc/letsencrypt/", "/etc/ssl/"]

# Startup script
CMD ["/run.sh"]