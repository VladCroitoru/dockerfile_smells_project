FROM openresty/openresty:latest-xenial
RUN apt-get update -qq && apt-get install -qqy libssl-dev git
RUN /usr/local/openresty/luajit/bin/luarocks install lapis 1.5.1-1 && \
/usr/local/openresty/luajit/bin/luarocks install lapis-console && \
/usr/local/openresty/luajit/bin/luarocks install penlight && \
/usr/local/openresty/luajit/bin/luarocks install inspect && \
/usr/local/openresty/luajit/bin/luarocks install datafile && \
/usr/local/openresty/luajit/bin/luarocks install date && \
/usr/local/openresty/luajit/bin/luarocks install https://raw.githubusercontent.com/vadi2/fhir-formats/master/fhirformats-0.1.0-1.rockspec
COPY . /opt/dryfhir
VOLUME /opt/dryfhir
WORKDIR /opt/dryfhir
ENTRYPOINT ["/usr/local/openresty/luajit/bin/lapis"]
CMD ["server", "dockerdev"]
