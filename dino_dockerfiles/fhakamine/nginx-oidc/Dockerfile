FROM openresty/openresty:centos

# DOWNLOAD DEPENDENCIES AND INSTALL OPENIDC
ENV LUA_RESTY_OPENIDC_VERSION=""
RUN yum install openssl-devel openssl git -y
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-openidc ${LUA_RESTY_OPENIDC_VERSION}

# GENERATE SELF-SIGNED certificate for 127.0.0.1.xip.io
RUN openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=US/ST=CA/L=Redwood City/O=ICE/CN=*.xip.io" \
    -keyout /etc/ssl/certs/nginx_server.key  -out /etc/ssl/certs/nginx_server.crt
ENV HOST=127.0.0.1.xip.io
ENV REVERSE_ACCESS='https://requestb.in/'
ENV REVERSE_API='https://requestb.in/'
ENV API_SCOPE='reqbin:get'

# COPY DEFAULT CONFIG
COPY config/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
EXPOSE 443

#COMMAND WRAPPER
COPY run.sh run.sh
RUN chmod +x run.sh
CMD ./run.sh
