FROM yangm97/lua:5.3-alpine

WORKDIR /data

ENTRYPOINT ["luacheck"]

CMD ["."]

RUN luarocks install luacheck
