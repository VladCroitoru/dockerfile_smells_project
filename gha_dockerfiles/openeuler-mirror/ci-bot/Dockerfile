FROM openeuler/openeuler:20.03 AS builder

COPY . /go/src/gitee.com/openeuler/ci-bot

ENV GOROOT=/usr/local/go
ENV PATH=$PATH:$GOROOT/bin
ENV GOPATH=/go

RUN yum -y update && \
    yum install -y wget && \
    yum install -y tar && \
    wget -O go.tar.gz https://golang.org/dl/go1.12.1.linux-amd64.tar.gz && \
    tar --remove-files -C /usr/local -zxf go.tar.gz && \
    CGO_ENABLED=1 go build -v -o /usr/local/bin/ci-bot -ldflags="-w -s -extldflags -static" gitee.com/openeuler/ci-bot/cmd/cibot

RUN mkdir -p /bot

WORKDIR /bot

COPY ./_service /bot

EXPOSE 8888

ENTRYPOINT ["ci-bot"]
