FROM quay.io/aptible/ubuntu:12.04

RUN apt-install git build-essential curl

ENV BUILD_DIR="/build"
ENV DEPLOY_TO="${BUILD_DIR}/out"

ENV GODIST="${BUILD_DIR}/godist"
ENV GOROOT="${GODIST}/go"
ENV GOPATH="${BUILD_DIR}/gopath"

ENV PATH="${GOPATH}/bin:${GOROOT}/bin:${PATH}"

ENV CADVISOR_DIR="${GOPATH}/src/github.com/google/cadvisor"

ENV GOLANG_VERSION=1.6
ENV GOLANG_DOWNLOAD_URL="https://golang.org/dl/go${GOLANG_VERSION}.linux-amd64.tar.gz"
ENV GOLANG_DOWNLOAD_SHA256="5470eac05d273c74ff8bac7bef5bad0b5abbd1c4052efbdbc8db45332e836b0b"

WORKDIR "$BUILD_DIR"

RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz && \
    echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - && \

    mkdir -p "$GODIST" && \
    tar -C "$GODIST" -xzf golang.tar.gz && \
    rm golang.tar.gz && \

    # Get Go build dependencies
    go get github.com/tools/godep

WORKDIR "$CADVISOR_DIR"

ADD . "$CADVISOR_DIR"
