FROM golang:1.8-alpine3.6
RUN apk update && apk add git
RUN go get -t github.com/rahulsom/kubehosts
CMD ["/go/bin/kubehosts"]
