FROM centos:6.7
 
RUN yum clean all && \
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-* && \
yum install -y epel-release && \
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6 && \
yum makecache && \
yum install -y pcre-devel openssl-devel zlib-devel gd-devel tar gcc wget git
 
RUN groupadd --system www && \
useradd --system --gid www www && \
mkdir -p {/var/log/wwwlogs,/var/run/nginx,/var/lock}
 
RUN wget -c http://nginx.org/download/nginx-1.9.5.tar.gz && \
git clone https://github.com/cuber/ngx_http_google_filter_module.git && \
git clone https://github.com/yaoweibin/ngx_http_substitutions_filter_module.git && \
git clone https://github.com/aperezdc/ngx-fancyindex.git
 
RUN tar xf nginx-1.9.5.tar.gz && \
cd nginx-1.9.5 && \
./configure --prefix=/usr/local/nginx \
--user=www --group=www \
--error-log-path=/var/log/wwwlogs/error.log \
--http-log-path=/var/log/wwwlogs/access.log \
--pid-path=/var/run/nginx/nginx.pid \
--lock-path=/var/lock/nginx.lock \
--with-pcre \
--with-ipv6 \
--with-http_ssl_module \
--with-http_flv_module \
--with-http_v2_module \
--with-http_realip_module \
--with-http_gzip_static_module \
--with-http_stub_status_module \
--with-http_mp4_module \
--with-http_image_filter_module \
--with-http_addition_module \
--http-client-body-temp-path=/usr/local/nginx/client/ \
--http-proxy-temp-path=/usr/local/nginx/proxy/ \
--http-fastcgi-temp-path=/usr/local/nginx/fcgi/ \
--http-uwsgi-temp-path=/usr/local/nginx/uwsgi \
--http-scgi-temp-path=/usr/local/nginx/scgi \
--add-module=../ngx_http_google_filter_module \
--add-module=../ngx_http_substitutions_filter_module \
--add-module=../ngx-fancyindex && \
make -j $(awk '/processor/{i++}END{print i}' /proc/cpuinfo) && make install && \
rm -rf ../{ngx_http*,ngx-fancyindex,nginx-1.9.5*}
 
ADD nginx.conf /usr/local/nginx/conf/nginx.conf
 
ADD run.sh /run.sh
RUN chmod +x /run.sh
 
VOLUME ["/home/wwwroot", "/usr/local/nginx/conf/ssl", "/usr/local/nginx/conf/vhost"]
 
EXPOSE 80 443
 
ENTRYPOINT ["/run.sh"]
 
CMD ["nginx"]
