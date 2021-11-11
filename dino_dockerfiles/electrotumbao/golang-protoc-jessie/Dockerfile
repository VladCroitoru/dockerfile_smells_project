FROM golang:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends wamerican && \
    apt-get clean

RUN apt-get update && \
    apt-get install -y --no-install-recommends unzip && \
    mkdir -pv /tmp/bin && \
    cd /tmp/bin && \
    wget https://github.com/google/protobuf/releases/download/v3.0.0-beta-3/protoc-3.0.0-beta-3-linux-x86_64.zip && \
    unzip protoc-3.0.0-beta-3-linux-x86_64.zip && \
    cp -v ./protoc /usr/bin/ && \
    cd / && \
    rm -rfv /tmp/bin && \

    apt-get clean && \

    GOPATH=/go && \
    mkdir -pv $GOPATH && \
    GOPATH=$GOPATH go get -u github.com/golang/protobuf/protoc-gen-go && \
    cp -v /go/bin/protoc-gen-go /usr/bin/ && \
    rm -rfv $GOPATH

