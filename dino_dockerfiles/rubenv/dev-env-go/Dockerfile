FROM rubenv/dev-env-vim

RUN dnf install -y autoconf automake libtool curl git unzip make gcc-c++ golang docker && \
    cd /tmp && \
    git clone https://github.com/google/protobuf.git && \
    cd /tmp/protobuf/ && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make check && \
    make install && \
    rm -rf /tmp/protobuf/ && cd && \
    dnf -y remove autoconf automake libtool unzip gcc-c++ && \
    dnf clean all && \
    mkdir -p /go && \
    export GOPATH=/go && \
    go get -v github.com/gengo/grpc-gateway/protoc-gen-grpc-gateway && \
    go get -v github.com/gengo/grpc-gateway/protoc-gen-swagger && \
    go get -v github.com/gogo/protobuf/protoc-gen-gogo && \
    go get -v github.com/golang/protobuf/protoc-gen-go && \
    curl http://downloads.drone.io/drone-cli/drone_linux_amd64.tar.gz | tar zx && \
    install -t /usr/local/bin drone && \
    rm drone

ENV GOPATH /go
ENV PATH /go/bin:/usr/local/bin:/usr/bin
