FROM ubuntu:xenial

MAINTAINER Tobias Gerschner <tobias.gerschner@gmail.com>

ENV RUST_VERSION 1.8.0
ENV RUST_BINARY_NAME rust-${RUST_VERSION}-x86_64-unknown-linux-gnu
ENV RUST_BINARY_URL https://static.rust-lang.org/dist/${RUST_BINARY_NAME}.tar.gz

RUN apt-get update && apt-get upgrade -y  && apt-get install wget -y

RUN cd /tmp && \
    wget ${RUST_BINARY_URL}

RUN cd /tmp && \
    tar -xf ${RUST_BINARY_NAME}.tar.gz

RUN cd /tmp/${RUST_BINARY_NAME} && \
    sh install.sh

RUN cd /tmp && \
    rm -rf ${RUST_BINARY_NAME} ${RUST_BINARY_NAME}.tar.gz

CMD ["rustc"]
