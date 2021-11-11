# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# A lot of the code here is "borrowed" from the
# https://github.com/googleapis/google-cloud-cpp project.

FROM ubuntu:focal
ARG NCPU=4

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get --no-install-recommends install -y \
        apt-transport-https \
        apt-utils \
        automake \
        build-essential \
        ca-certificates \
        clang-10 \
        clang-format-10 \
        clang-tidy-10 \
        cmake \
        curl \
        g++ \
        gawk \
        gcc \
        git \
        less \
        libc-ares-dev \
        libc-ares2 \
        libcurl4-openssl-dev \
        libssl-dev \
        libtool \
        llvm-10 \
        lsb-release \
        m4 \
        make \
        ninja-build \
        patch \
        pkg-config \
        python3 \
        python3-dev \
        python3-pip \
        tar \
        unzip \
        vim \
        wget \
        zip \
        zlib1g-dev

# Install Python packages
RUN update-alternatives --install /usr/bin/python python $(which python3) 10
RUN pip3 install setuptools wheel pylint

# Install the Cloud SDK and some of the emulators. We use the emulators to run
# integration tests.
COPY install-cloud-sdk.sh /var/tmp/ci/
WORKDIR /var/tmp/downloads
RUN /var/tmp/ci/install-cloud-sdk.sh
ENV CLOUD_SDK_LOCATION=/usr/local/google-cloud-sdk
ENV PATH=${CLOUD_SDK_LOCATION}/bin:${PATH}

# PyTorch is compiled with `_GLIBCXX_USE_CXX11_ABI` set to `0`,
# which means that our C++ Bigtable plugin and all its dependencies have to be
# compiled that way too. For more information please refer to the section
# 'Note on glibc++ ABI' in README.md

# In order to make it easy for the users, we compile the plugin and its
# dependecies statically. This is especially helpful given the
# `_GLIBCXX_USE_CXX11_ABI` incompatibility. However, the end result is a library
# loaded by python, so we need to compile the code as position independent
# (hence CMAKE_POSITION_INDEPENDENT_CODE is set to ON).

# libre2 is required by gRPC
WORKDIR /var/tmp/build/re2
RUN curl -sSL https://github.com/google/re2/archive/refs/tags/2021-08-01.tar.gz | \
    tar -xzf - --strip-components=1 && \
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=NO \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DCRC32C_BUILD_TESTS=OFF \
        -DCRC32C_BUILD_BENCHMARKS=OFF \
        -DCRC32C_USE_GLOG=OFF \
        -DCMAKE_CXX_FLAGS='-D_GLIBCXX_USE_CXX11_ABI=0' \
        -H. -Bcmake-out && \
    cmake --build cmake-out -- -j ${NCPU:-4} && \
    cmake --build cmake-out --target install -- -j ${NCPU:-4} && \
    ldconfig

# Abseil
WORKDIR /var/tmp/build/abseil-cpp
RUN curl -sSL https://github.com/abseil/abseil-cpp/archive/20210324.2.tar.gz | \
    tar -xzf - --strip-components=1 && \
    sed -i 's/^#define ABSL_OPTION_USE_\(.*\) 2/#define ABSL_OPTION_USE_\1 0/' "absl/base/options.h" && \
    CXXFLAGS='-D_GLIBCXX_USE_CXX11_ABI=0' \
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_TESTING=OFF \
        -DBUILD_SHARED_LIBS=NO \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DCMAKE_CXX_STANDARD=11 \
        -H. -Bcmake-out && \
    cmake --build cmake-out -- -j ${NCPU:-4} && \
    cmake --build cmake-out --target install -- -j ${NCPU:-4} && \
    ldconfig

# Protobuf

# We need to install a version of Protobuf that is recent enough to support the
# Google Cloud Platform proto files:
WORKDIR /var/tmp/build/protobuf
RUN curl -sSL https://github.com/protocolbuffers/protobuf/archive/v3.17.3.tar.gz | \
    tar -xzf - --strip-components=1 && \
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=no \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -Dprotobuf_BUILD_TESTS=OFF \
        -DCMAKE_CXX_FLAGS='-D_GLIBCXX_USE_CXX11_ABI=0' \
        -Hcmake -Bcmake-out && \
    cmake --build cmake-out -- -j ${NCPU:-4} && \
    cmake --build cmake-out --target install -- -j ${NCPU:-4} && \
    ldconfig

# gRPC
WORKDIR /var/tmp/build/grpc
RUN curl -sSL https://github.com/grpc/grpc/archive/v1.39.0.tar.gz | \
    tar -xzf - --strip-components=1 && \
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DgRPC_INSTALL=ON \
        -DgRPC_BUILD_TESTS=OFF \
        -DgRPC_ABSL_PROVIDER=package \
        -DgRPC_CARES_PROVIDER=package \
        -DgRPC_PROTOBUF_PROVIDER=package \
        -DgRPC_RE2_PROVIDER=package \
        -DgRPC_SSL_PROVIDER=package \
        -DgRPC_ZLIB_PROVIDER=package \
        -DBUILD_SHARED_LIBS=no \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DCMAKE_CXX_FLAGS='-D_GLIBCXX_USE_CXX11_ABI=0' \
        -H. -Bcmake-out && \
    cmake --build cmake-out -- -j ${NCPU:-4} && \
    cmake --build cmake-out --target install -- -j ${NCPU:-4} && \
    ldconfig

# crc32c
WORKDIR /var/tmp/build/crc32c
RUN curl -sSL https://github.com/google/crc32c/archive/1.1.0.tar.gz | \
    tar -xzf - --strip-components=1 && \
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=NO \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DCRC32C_BUILD_TESTS=OFF \
        -DCRC32C_BUILD_BENCHMARKS=OFF \
        -DCRC32C_USE_GLOG=OFF \
        -DCMAKE_CXX_FLAGS='-D_GLIBCXX_USE_CXX11_ABI=0' \
        -H. -Bcmake-out && \
    cmake --build cmake-out -- -j ${NCPU:-4} && \
    cmake --build cmake-out --target install -- -j ${NCPU:-4} && \
    ldconfig

# nlohmann_json
WORKDIR /var/tmp/build/json
RUN curl -sSL https://github.com/nlohmann/json/archive/v3.9.1.tar.gz | \
    tar -xzf - --strip-components=1 && \
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_SHARED_LIBS=no \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DBUILD_TESTING=OFF \
        -H. -Bcmake-out/nlohmann/json && \
    cmake --build cmake-out/nlohmann/json --target install -- -j ${NCPU:-4} && \
    ldconfig

# google-cloud-cpp
WORKDIR /var/tmp/build/google-cpp
RUN curl -sSL \
  https://github.com/googleapis/google-cloud-cpp/archive/refs/tags/v1.30.1.tar.gz  | \
  tar xfvz - && \
  cd google-cloud-cpp-1.30.1 && \
  cmake -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DBUILD_TESTING=OFF \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DGOOGLE_CLOUD_CPP_ENABLE_EXAMPLES=OFF \
        -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
        -DCMAKE_CXX_FLAGS='-D_GLIBCXX_USE_CXX11_ABI=0' \
        -H. -B cmake-out && \
  cmake --build cmake-out -j ${NCPU:-4} && \
  cmake --install cmake-out --component google_cloud_cpp_development && \
  ldconfig

# PyTorch
RUN pip3 install \
      torch==1.10.0+cpu \
      -f https://download.pytorch.org/whl/torch_stable.html

WORKDIR /opt/pytorch
