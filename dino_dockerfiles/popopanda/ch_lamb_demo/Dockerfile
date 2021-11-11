FROM golang:alpine

EXPOSE 8090
ENV GOPATH /opt/gotools

WORKDIR /opt

ADD go/src/github.com/ch/helloworld.go /opt/helloworld.go

RUN apk add --no-cache curl && \
  mkdir $GOPATH

CMD ["go", "run", "/opt/helloworld.go"]
