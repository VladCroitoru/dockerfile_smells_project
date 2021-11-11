FROM alpine:3.4

RUN apk update && apk add ca-certificates
RUN rm -rf /var/cache/apk/*

ADD drone-spark /bin/

ENTRYPOINT ["/bin/drone-spark"]
