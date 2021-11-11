FROM alpine

RUN apk add --no-cache ca-certificates

ADD gopath/bin/transitdb /transitdb

CMD ["/transitdb"]
