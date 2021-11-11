FROM alpine:latest
MAINTAINER Rick Gaiser <rgaiser@gmail.com>

WORKDIR /build

ENV PS2DEV /usr/local/ps2dev
ENV PS2SDK $PS2DEV/ps2sdk
ENV GSKIT  $PS2DEV/gsKit
ENV PATH   $PATH:${PS2DEV}/bin:${PS2DEV}/ee/bin:${PS2DEV}/iop/bin:${PS2DEV}/dvp/bin:${PS2SDK}/bin

RUN \
  apk add --no-cache make git ucl gawk zip && \
  apk add --no-cache --virtual .build-deps bash gcc musl-dev patch wget zlib-dev ucl-dev && \

  git clone --depth 1 https://github.com/ps2dev/ps2toolchain && \
  cd ps2toolchain && \
    ./toolchain.sh 1 && \
    ./toolchain.sh 2 && \
    ./toolchain.sh 3 && \
    ./toolchain.sh 4 && \
    ./toolchain.sh 5 && \
    cd .. && \
  rm -Rf ps2toolchain && \

  git clone --depth 1 https://github.com/ps2dev/gsKit && \
  cd gsKit && \
    make install && \
    cd .. && \
  rm -Rf gsKit && \

  git clone --depth 1 https://github.com/ps2dev/ps2sdk-ports && \
  cd ps2sdk-ports && \
    make zlib && \
    make libpng && \
    make libjpeg && \
    make freetype-2.4.12 && \
    cd .. && \
  rm -Rf ps2sdk-ports && \

  git clone --depth 1 https://github.com/ps2dev/ps2-packer && \
  cd ps2-packer && \
    make install && \
    cd .. && \
  rm -Rf ps2-packer && \

  apk del .build-deps && \
  rm -rf tmp/*

