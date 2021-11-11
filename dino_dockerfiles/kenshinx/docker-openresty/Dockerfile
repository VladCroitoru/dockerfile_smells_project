# Dockerfile for Openresty-1.4.3.4 with luajit-2.0.3 base centos 6.5

FROM hnakamur/centos

MAINTAINER kenshin kenshin.acs@gmail.com

RUN yum update -y

RUN yum install -y gcc
RUN yum install -y gcc-c++
RUN yum install -y openssl-devel
RUN yum install -y perl

#Install luajit 2.0
RUN wget http://luajit.org/download/LuaJIT-2.0.3.tar.gz
RUN tar zxvf LuaJIT-2.0.3.tar.gz
RUN (cd LuaJIT-2.0.3 && make && make install)

#Install pcre
RUN wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.34.tar.gz
RUN tar zxvf pcre-8.34.tar.gz
RUN (cd pcre-8.34 && ./configure && make && make install)

#Install Openresty
RUN wget http://openresty.org/download/ngx_openresty-1.4.3.6.tar.gz
RUN tar zxvf ngx_openresty-1.4.3.6.tar.gz
RUN (cd ngx_openresty-1.4.3.6 && ./configure --with-luajit)
RUN (cd ngx_openresty-1.4.3.6 && gmake && gmake install)

#Configuration nginx
RUN ln -s /usr/local/openresty/nginx/sbin/nginx /usr/local/bin/nginx
RUN mkdir -p /etc/nginx
RUN cp -r /usr/local/openresty/nginx/conf/* /etc/nginx/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN ln -s /usr/local/lib/libpcre.so.1 /lib64

#ENTRYPOINT ["nginx", "-c", "/etc/nginx/nginx.conf"]

EXPOSE 80 443



