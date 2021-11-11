FROM golang:alpine

RUN apk update && \
    apk add binutils && \

    mkdir -pv /tmp/src && \
    cd /tmp/src && \
    wget http://mirrors.kernel.org/ubuntu/pool/main/s/scowl/wamerican_7.1-1_all.deb && \
    ar x wamerican_7.1-1_all.deb && \
    tar -zxf data.tar.gz && \
    cp -rv ./usr/share/dict /usr/share/ && \
    rm -rf /tmp/src && \

    apk del binutils && \
    rm -rf /var/cache/apk/*

RUN apk update && \
    PACKAGES='bash ca-certificates gcc g++ make musl-dev libtool git autoconf automake' && \
    apk add $PACKAGES && \

    mkdir -pv /tmp/src && \
    cd /tmp/src && \
    wget https://github.com/google/protobuf/archive/v3.0.0-beta-3.tar.gz && \
    tar -zxf v3.0.0-beta-3.tar.gz && \
    cd ./protobuf-3.0.0-beta-3 && \
    ./autogen.sh && \
    ./configure --prefix=/usr --disable-shared && \
    make -j 2 && \
    make install && \
    cd / && \
    rm -rf /tmp/src && \
    apk add libstdc++ libgcc && \

    GOPATH=/go && \
    mkdir -pv $GOPATH && \
    GOPATH=$GOPATH go get -u github.com/golang/protobuf/protoc-gen-go && \
    cp /go/bin/protoc-gen-go /usr/bin/ && \
    rm -rf $GOPATH && \

    apk del $PACKAGES && \
    rm -rf /var/cache/apk/*
