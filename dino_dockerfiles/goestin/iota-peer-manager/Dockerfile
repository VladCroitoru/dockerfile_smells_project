FROM jkilbride/node-npm-alpine:8

RUN npm i -g iota-pm 

EXPOSE 8888/tcp
STOPSIGNAL 9

ENTRYPOINT ["iota-pm"]
