FROM docker:18-git

ENV GO111MODULE off
ENV GOPATH /go
ENV GOBIN "${GOPATH}/bin"
ENV PATH "${GOBIN}:${PATH}"

RUN apk update && apk add --no-cache go=1.12.12-r0 alpine-sdk bash && apk upgrade && \
    mkdir -p ${GOBIN} && \
    mkdir -p ~/.ssh && chmod 0700 ~/.ssh && \
    curl -s https://glide.sh/get | sh && \
    curl -s https://raw.githubusercontent.com/golang/dep/master/install.sh | sh && \
    go get github.com/huanteng/pgdiff && \
    go clean -cache -testcache -modcache && \
    rm -rf ${GOPATH}/src/* && \
    rm -rf /tmp/*
