FROM golang:1.13.0 as protoc_builder

ENV GRPC_VERSION=1.23.0 \
    GOPATH=/go \
    PATH=$PATH:/go/bin/

RUN mkdir -p /go/bin
COPY . $GOPATH/src/github.com/xissy/protoc
WORKDIR $GOPATH/src/github.com/xissy/protoc

RUN curl https://glide.sh/get | sh
RUN glide install
RUN cd vendor/github.com/golang/protobuf && make all
RUN cd vendor/github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway && \
        glide init --non-interactive && \
        glide install && \
        go install
RUN cd vendor/github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger && \
        glide init --non-interactive && \
        glide install && \
        go install
RUN go get github.com/ckaznocha/protoc-gen-lint
RUN go get github.com/xissy/protoc-gen-swiftgrpcrx
RUN go install github.com/xissy/protoc-gen-swiftgrpcrx


FROM swift:4.2.1 as swift_builder
RUN apt update && apt install -y libnghttp2-dev
ENV SWIFT_GRPC_VERSION=master \
    SWIFT_GRPC_REPO=grpc
WORKDIR /
RUN git clone -b ${SWIFT_GRPC_VERSION} https://github.com/${SWIFT_GRPC_REPO}/grpc-swift && \
    cd grpc-swift && \
    make


FROM swift:4.2.1

RUN export DEBIAN_FRONTEND=noninteractive DEBCONF_NONINTERACTIVE_SEEN=true && apt-get -q update && \
    apt-get -q install -y \
    build-essential \
    automake \
    autoconf \
    curl \
    libtool \
    libnghttp2-dev \
    unzip \
    && rm -r /var/lib/apt/lists/*

ENV PROTOBUF_VERSION=3.9.1 \
    GRPC_VERSION=1.23.0 \
    GOPATH=/go \
    PATH=$PATH:/go/bin/ \
    GRPC_JAVA_VERSION=1.23.0 \
    GRPC_WEB_VERSION=1.0.6 \
    OUTDIR=/out

RUN curl -O -L https://github.com/google/protobuf/releases/download/v${PROTOBUF_VERSION}/protoc-${PROTOBUF_VERSION}-linux-x86_64.zip \
    && unzip protoc-${PROTOBUF_VERSION}-linux-x86_64.zip -d /usr \
    && rm -rf protoc-${PROTOBUF_VERSION}-linux-x86_64.zip

RUN mkdir -p /protobuf && \
        curl -L https://github.com/google/protobuf/archive/v${PROTOBUF_VERSION}.tar.gz | tar xvz --strip-components=1 -C /protobuf
RUN git clone --depth 1 --recursive -b v${GRPC_VERSION} https://github.com/grpc/grpc.git /grpc && \
        rm -rf grpc/third_party/protobuf && \
        ln -s /protobuf /grpc/third_party/protobuf
RUN mkdir -p /grpc-java && \
        curl -L https://github.com/grpc/grpc-java/archive/v${GRPC_JAVA_VERSION}.tar.gz | tar xvz --strip-components=1 -C /grpc-java
RUN mkdir -p /grpc-web && \
        curl -L https://github.com/grpc/grpc-web/archive/${GRPC_WEB_VERSION}.tar.gz | tar xvz --strip-components=1 -C /grpc-web
RUN cd /protobuf && \
        autoreconf -f -i -Wall,no-obsolete && \
        ./configure --prefix=/usr --enable-static=no && \
        make -j2 && make install
RUN cd /grpc-java/compiler/src/java_plugin/cpp && \
        g++ \
        -I. -I/protobuf/src \
        *.cpp \
        -L/protobuf/src/.libs \
        -lprotoc -lprotobuf -lpthread --std=c++0x -s \
        -o protoc-gen-grpc-java
RUN cd /protobuf && \
        make install DESTDIR=${OUTDIR}
RUN cd /grpc && \
        make install-plugins prefix=${OUTDIR}/usr
RUN cd /grpc-java/compiler/src/java_plugin/cpp && \
        install -c protoc-gen-grpc-java ${OUTDIR}/usr/bin/
RUN cd /grpc-web/javascript/net/grpc/web && \
        make && \
        install protoc-gen-grpc-web ${OUTDIR}/usr/bin/
RUN find ${OUTDIR} -name "*.a" -delete -or -name "*.la" -delete
RUN cp -R ${OUTDIR}/usr /

COPY --from=protoc_builder $GOPATH/bin $GOPATH/bin
COPY --from=protoc_builder \
        $GOPATH/src/github.com/xissy/protoc/vendor/github.com/grpc-ecosystem/grpc-gateway \
        $GOPATH/src/github.com/grpc-ecosystem/grpc-gateway
COPY --from=swift_builder /grpc-swift /grpc-swift
RUN for p in protoc-gen-swift protoc-gen-swiftgrpc; do \
        ln -s /grpc-swift/${p} /usr/bin/${p}; \
    done

ENTRYPOINT ["protoc"]
