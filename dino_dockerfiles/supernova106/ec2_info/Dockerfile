FROM golang:latest

ENV GOPATH /go

RUN mkdir -p "$GOPATH/src/ec2_info"
ADD . "$GOPATH/src/github.com/supernova106/ec2_info"

WORKDIR $GOPATH/src/github.com/supernova106/ec2_info/app
RUN chmod +x script/*
RUN ./script/build

CMD ./app
