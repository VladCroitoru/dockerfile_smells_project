FROM golang:1.7

COPY . /go/src/github.com/guilhem/patakube
COPY templates/config.sh /templates/config.sh

RUN go install github.com/guilhem/patakube

EXPOSE 8080

ENTRYPOINT ["/go/bin/patakube"]
