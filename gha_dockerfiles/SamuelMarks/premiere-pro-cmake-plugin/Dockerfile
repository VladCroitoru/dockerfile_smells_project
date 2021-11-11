FROM debian:stable-slim as build

LABEL description="Build container"

RUN echo 'deb-src http://deb.debian.org/debian buster main' >> /etc/apt/sources.list \
    && apt-get update -qq \
    && apt-get install -y  \
    autoconf \
    binutils \
    build-essential \
    curl \
    gcc \
    g++ \
    git \
    libstdc++6 \
    libtool \
    make \
    ninja-build \
    pkg-config \
    tar \
    unzip \
    zip \
    && apt-get -y build-dep cmake \
    && curl 'https://github.com/Kitware/CMake/releases/download/v3.21.2/cmake-3.21.2-linux-x86_64.sh' -Lo '/tmp/cmake.sh' \
    && chmod +x '/tmp/cmake.sh' \
    && '/tmp/cmake.sh' --prefix='/usr/local' --skip-license

COPY ./ /pp

WORKDIR /pp/build

# See Dockerfile.base for how to form this directory, then
# `tar czf linux_vcpkg.tar.gz <path to vcpkg directory>`
# (I did so, but with rsync over SSH to a VM… Docker is still flakey)
ADD 'linux_vcpkg.tar.gz' /vcpkg

# See README.md for where to find this .zip file
ADD 'Premiere_Pro_CC_13_Mac_SDK.zip' /pp_sdk

RUN cmake .. \
          -DCMAKE_BUILD_TYPE='Debug' \
          -DCMAKE_TOOLCHAIN_FILE='/vcpkg/scripts/buildsystems/vcpkg.cmake' \
          -DCRYPTO_LIB='OpenSSL' \
          -DADOBE_PP_SDK='/pp_sdk/Premiere Pro CC 13.0 Mac SDK' \
    && cmake . --build

FROM alpine:latest as runtime

LABEL description="Run container"

RUN apk update && apk add --no-cache \
    libstdc++

COPY --from=build '/src/build/pp' '/usr/local/pp/pp'

WORKDIR /usr/local/pp

CMD ./pp

EXPOSE 8080
