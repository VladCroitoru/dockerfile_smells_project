FROM alpine

RUN apk add --update --no-cache libstdc++ && \
    apk add --no-cache --virtual .build-dependencies git make g++ unzip autoconf automake libtool file openssl curl cmake && \
    git clone https://github.com/grpc/grpc && \
    cd /grpc && \
    git submodule update --init && \
    cd third_party/gflags/ && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install && \
    cd /grpc && \
    make grpc_cli -j4 && \
    cp bins/opt/grpc_cli /bin && \
    apk del --no-cache --purge .build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /grpc

