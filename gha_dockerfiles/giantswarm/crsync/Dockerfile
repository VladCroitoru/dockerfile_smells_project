FROM docker

RUN apk add --no-cache ca-certificates

ADD ./crsync /crsync

ENTRYPOINT ["/crsync"]
