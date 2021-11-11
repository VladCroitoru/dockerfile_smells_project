FROM openresty/openresty:1.11.2.1-trusty

LABEL maintainer="Saagie"

RUN apt-get update && apt-get install -y libssl-dev git  && rm -rf /var/lib/apt/lists/*
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-http
RUN /usr/local/openresty/luajit/bin/luarocks install luajwt
RUN /usr/local/openresty/luajit/bin/luarocks install lua-cjson
RUN /usr/local/openresty/luajit/bin/luarocks install lua-resty-cookie