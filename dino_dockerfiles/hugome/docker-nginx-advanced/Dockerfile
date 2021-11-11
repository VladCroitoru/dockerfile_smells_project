FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y wget build-essential \
			libpcre3 libpcre3-dev zlib1g-dev libssl-dev
RUN mkdir /tmp/build
WORKDIR /tmp/build

RUN wget "https://github.com/openresty/headers-more-nginx-module/archive/v0.30.tar.gz"
RUN wget "http://nginx.org/download/nginx-1.9.15.tar.gz"

RUN tar zvfx nginx-1.9.15.tar.gz
RUN tar zvfx v0.30.tar.gz
RUN useradd nginx

WORKDIR nginx-1.9.15
RUN  ./configure						\
	--user=nginx                          			\
	--group=nginx                         			\
	--prefix=/etc/nginx                   			\
	--sbin-path=/usr/sbin/nginx           			\
	--conf-path=/etc/nginx/nginx.conf     			\
	--pid-path=/var/run/nginx.pid         			\
	--lock-path=/var/run/nginx.lock       			\
	--error-log-path=/var/log/nginx/error.log 		\
	--http-log-path=/var/log/nginx/access.log 		\
	--add-module=/tmp/build/headers-more-nginx-module-0.30/	\
	--with-http_gzip_static_module				\
	--with-http_stub_status_module 				\
	--with-http_ssl_module 					\
	--with-pcre 						\
	--with-file-aio 					\
	--with-http_realip_module 				\
	--without-http_scgi_module --without-http_uwsgi_module	\
	--without-http_fastcgi_module

RUN make install
EXPOSE 80 443
VOLUME ["/var/log/nginx/", "/etc/nginx/"]
CMD ["nginx", "-g", "daemon off;"]
