#FROM japaric/x86_64-unknown-linux-musl:latest
FROM bitnami/minideb:jessie
MAINTAINER Angus Lees <gus@inodes.org>

RUN install_packages \
 wget patch git-core gcc g++ make gawk bzip2 gzip xz-utils ca-certificates \
 libgmp-dev libmpfr-dev libmpc-dev \
 cmake pkg-config curl

RUN \
 set -ex; \
 cd /tmp; \
 git clone https://github.com/GregorR/musl-cross; \
 cd musl-cross; \
 ./build.sh; \
 cd /; \
 rm -r /tmp/musl-cross

ENV PATH=$PATH:/opt/cross/x86_64-linux-musl/bin

RUN \
 set -ex; \
 cd /tmp; \
 curl -LSfs http://japaric.github.io/trust/install.sh | \
    sh -s -- --git japaric/xargo --tag v0.3.5 --target x86_64-unknown-linux-gnu --to /usr/bin

RUN \
 set -ex; \
 mkdir /tmp/openssl; \
 cd /tmp/openssl; \
 install_packages m4 make perl curl ca-certificates; \
 curl -LSfs https://www.openssl.org/source/openssl-1.0.2k.tar.gz | \
        tar --strip-components=1 -xz; \
 AR=x86_64-linux-musl-ar CC=x86_64-linux-musl-gcc ./Configure \
   --prefix=/openssl \
   no-dso \
   linux-x86_64 \
   -fPIC \
   -static; \
 make -j$(nproc); \
 make install; \
 cd /tmp; \
 rm -r /tmp/openssl

ENV CC_x86_64_unknown_linux_musl=x86_64-linux-musl-gcc \
    CXX_x86_64_unknown_linux_musl=x86_64-linux-musl-g++ \
    OPENSSL_DIR=/openssl \
    OPENSSL_INCLUDE_DIR=/openssl/include \
    OPENSSL_LIB_DIR=/openssl/lib
