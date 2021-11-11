FROM amazonlinux:2 as builder

ARG GO_FILE=go1.17.1.linux-amd64.tar.gz
ARG SRC_MODULE=github.com/mkaiho/gin-sample

ENV GOPATH /go
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin

WORKDIR $GOPATH/src/$SRC_MODULE
COPY ./Makefile $GOPATH/src/$SRC_MODULE
COPY ./go.mod $GOPATH/src/$SRC_MODULE
COPY ./go.sum $GOPATH/src/$SRC_MODULE
COPY ./domain $GOPATH/src/$SRC_MODULE/domain
COPY ./usecases $GOPATH/src/$SRC_MODULE/usecases
COPY ./interfaces $GOPATH/src/$SRC_MODULE/interfaces
COPY ./infrastructures $GOPATH/src/$SRC_MODULE/infrastructures
COPY ./cmd $GOPATH/src/$SRC_MODULE/cmd

RUN yum install -y curl tar make gzip \
  && curl -OL https://golang.org/dl/${GO_FILE} \
  && tar -C /usr/local -xzf ${GO_FILE} \
  && rm ${GO_FILE} \
  && make build-server

FROM amazonlinux:2

RUN yum update -y && yum install -y shadow-utils \
  && useradd "ec2-user"

USER ec2-user
WORKDIR /ec2-user

COPY --from=builder /go/src/github.com/mkaiho/gin-sample/build ./build

CMD ["./build/server"]