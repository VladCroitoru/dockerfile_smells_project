FROM golang:alpine

RUN apk add --no-cache ca-certificates apache2-utils

COPY . /go/src/ruyue/

WORKDIR /go/src/ruyue/

RUN go build .

CMD ["./ruyue"]