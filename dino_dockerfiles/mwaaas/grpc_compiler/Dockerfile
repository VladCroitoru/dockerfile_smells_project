FROM python:3.3.6

# Protobuf version
ENV PROTOBUF_VERSION="3.0.0"
ENV PROTOBUF_ZIP=protoc-${PROTOBUF_VERSION}-linux-x86_64.zip
ENV PROTOBUF_URL=https://github.com/google/protobuf/releases/download/v${PROTOBUF_VERSION}/${PROTOBUF_ZIP}

RUN apt-get update && apt-get install -y  \
    autoconf automake libtool curl g++ git make unzip \
    && cd /tmp \
    # install protobuf
    && wget ${PROTOBUF_URL} \
    && unzip ${PROTOBUF_ZIP} 'bin/*' -d /usr \
    && pip install grpcio==1.2.1 grpcio-tools==1.2.1\
    # Cleanup
    && rm -rf /tmp/* \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

CMD ["protoc"]