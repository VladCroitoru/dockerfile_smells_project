FROM centos:centos6
MAINTAINER David Pelaez <david@vlipco.co>

# this will handle unarchiving! no tar xzf needed
ADD misc/ngx_openresty-1.7.2.1.tar.gz /openresty

RUN cd /openresty/ngx_openresty-1.7.2.1 && \
	yum install -y perl pcre-dev pcre-devel openssl-devel gcc && ./configure && make install && \
	ln -s /usr/local/openresty/nginx/sbin/nginx /usr/bin/nginx && yum -y remove gcc

ADD conf /nginx/conf
RUN rm -rf /openresty && mkdir /nginx/logs

ADD misc/lua-resty-http-0.05.tar.gz /lua-resty-http
RUN cd /lua-resty-http/lua-resty-http-0.05 && make install
RUN mv /usr/local/lib/lua/resty/http/* /usr/local/lib/lua/resty/
RUN rm -rf /usr/local/lib/lua/resty/http/
RUN rm -rf /lua-resty-http

EXPOSE 80

CMD ["/usr/bin/nginx", "-p", "/nginx/", "-c", "conf/nginx.conf"]
