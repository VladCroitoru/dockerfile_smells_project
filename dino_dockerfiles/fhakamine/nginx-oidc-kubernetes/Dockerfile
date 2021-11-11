FROM openresty/openresty:centos

# DOWNLOAD DEPENDENCIES AND INSTALL OPENIDC
ENV LUA_RESTY_OPENIDC_VERSION=""
RUN yum install openssl-devel openssl git -y
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-openidc ${LUA_RESTY_OPENIDC_VERSION}

# DEFAULT ENVIRONMENT VARIABLES
ENV HOST=127.0.0.1.xip.io

# COPY DEFAULT CONFIG
COPY config/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

#COMMAND WRAPPER
COPY run.sh run.sh
RUN chmod +x run.sh
CMD ./run.sh
