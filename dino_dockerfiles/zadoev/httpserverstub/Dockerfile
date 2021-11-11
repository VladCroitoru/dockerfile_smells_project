FROM golang

ADD . /go/src/github.com/zadoev/httpserverstub/

RUN go install github.com/zadoev/httpserverstub

ENTRYPOINT /go/bin/httpserverstub

EXPOSE 8181