FROM openresty/openresty:trusty

RUN apt-get -y update && apt-get install -y git
RUN /usr/local/openresty/luajit/bin/luarocks install ledge

ENV LUA_PATH /usr/local/openresty/luajit/share/lua/5.1/ledge/?.lua;/usr/local/openresty/luajit/share/lua/5.1/?.lua

ENTRYPOINT ["/usr/local/openresty/bin/openresty", "-g", "daemon off;"]

