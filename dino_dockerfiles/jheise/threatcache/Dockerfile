FROM golang

RUN mkdir /go/src/threatcache

ADD *.go /go/src/threatcache/
RUN go get threatcache
RUN go install threatcache

ENV IPADDR 0.0.0.0
ENV PORT 8888
ENV REDISHOST redis
ENV REDISPORT 6379

EXPOSE ${PORT}
CMD /go/bin/threatcache -ipaddr ${IPADDR} -port ${PORT} -redishost ${REDISHOST} -redisport ${REDISPORT}
