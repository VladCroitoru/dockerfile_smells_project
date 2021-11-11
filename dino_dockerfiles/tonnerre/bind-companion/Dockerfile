FROM golang:alpine
LABEL maintainer="Caoimhe Chaos <caoimhechaos@protonmail.com>"

RUN apk --update add git bind protobuf make
RUN go get gopkg.in/fsnotify.v1
RUN go get github.com/golang/protobuf/proto
RUN cd /go/src/github.com/golang/protobuf/protoc-gen-go && go install
RUN mkdir -p /go/src/github.com/caoimhechaos/bind-companion
COPY companion.go /go/src/github.com/caoimhechaos/bind-companion/companion.go
COPY config.proto /go/src/github.com/caoimhechaos/bind-companion/config.proto
COPY bind-config.tmpl /etc/bind/named.conf.tmpl
RUN cd /go/src/github.com/caoimhechaos/bind-companion && protoc --go_out=. config.proto
RUN cd /go/src/github.com/caoimhechaos/bind-companion && go install
RUN chown named:named /etc/bind

EXPOSE 5353/tcp 5353/udp
VOLUME ["/etc/bind/git", "/etc/bind/slavezones", "/config"]
USER named

CMD ["/go/bin/bind-companion", "--config", "/config/bind.config"]
