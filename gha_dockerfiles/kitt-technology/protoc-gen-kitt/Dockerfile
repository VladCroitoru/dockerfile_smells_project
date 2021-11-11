FROM ubuntu:xenial

ENV INSTALL_DEPS \
  ca-certificates \
  gcc \
  git \
  make \
  software-properties-common \
  unzip \
  wget

RUN apt-get update \
  && apt-get install -y -q --no-install-recommends ${INSTALL_DEPS} \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# protoc
ENV PROTOC_VER=3.6.1
ENV PROTOC_REL=protoc-"${PROTOC_VER}"-linux-x86_64.zip
RUN wget https://github.com/google/protobuf/releases/download/v"${PROTOC_VER}/${PROTOC_REL}" \
  && unzip ${PROTOC_REL} -d protoc \
  && mv protoc /usr/local \
  && ln -s /usr/local/protoc/bin/protoc /usr/local/bin

# go
ENV GOROOT /usr/local/go
ENV GOPATH /go
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH
ENV GORELEASE go1.13.9.linux-amd64.tar.gz
RUN wget -q https://dl.google.com/go/$GORELEASE \
    && tar -C $(dirname $GOROOT) -xzf $GORELEASE \
    && rm $GORELEASE \
    && mkdir -p $GOPATH/{src,bin,pkg}

# protoc-gen-go
ENV PGG_PKG "google.golang.org/protobuf/cmd/protoc-gen-go"
ENV PGG_PATH "${GOPATH}/src/${PGG_PKG}"
ENV PGG_VER=v1.21.0
RUN go get -d ${PGG_PKG} \
  && cd ${PGG_PATH} \
  && git checkout ${PGG_VER} \
  && go install \
  && cd - \
  && rm -rf ${PGG_PATH}

# protoc-gen-grpc-go
ENV PGG_PKG "google.golang.org/grpc/cmd/protoc-gen-go-grpc"
ENV PGG_PATH "${GOPATH}/src/${PGG_PKG}"
ENV PGG_VER=v1.34.0
RUN go get -d ${PGG_PKG} \
  && cd ${PGG_PATH} \
  && git checkout ${PGG_VER} \
  && go install \
  && cd - \
  && rm -rf ${PGG_PATH}

COPY Makefile ./
COPY go.* ./

RUN make deps

CMD ["make", "test"]