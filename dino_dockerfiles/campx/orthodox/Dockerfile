FROM ubuntu:18.04

ENV VCPKG_ROOT="/opt/vcpkg"
ENV CLANG_VERSION=8
ENV GCC_VERSION=8

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    rsync \
    curl \
    locate \
    pkg-config \
    perl-modules \
    unzip \
    tar \
    vim \
    xz-utils \
    python \
    python-pip \
    gcc-${GCC_VERSION} \
    g++-${GCC_VERSION} \
    git \
    gdb \
    gcovr \
    llvm \
    ccache \
    clang-${CLANG_VERSION} \
    clang-tidy-${CLANG_VERSION} \
    clang-format-${CLANG_VERSION} \
    clang-tools-${CLANG_VERSION} \
    ninja-build \
    libdigest-md5-file-perl \
    libstdc++-8-dev \
    libc++-7-dev \
 && apt-get -y autoremove \
 && apt-get -y clean \
 && updatedb

RUN ln -s /usr/bin/clang-${CLANG_VERSION} /usr/bin/clang \
  && ln -s /usr/bin/clang++-${CLANG_VERSION} /usr/bin/clang++ \
  && ln -s /usr/bin/clang-tidy-${CLANG_VERSION} /usr/bin/clang-tidy \
  && ln -s /usr/bin/clang-format-${CLANG_VERSION} /usr/bin/clang-format

RUN python -m pip install --upgrade pip \
 && pip install requests \
 && pip install setuptools \
 && pip install wheel \
 && pip install pyyaml \
 && pip install cpp-coveralls

RUN wget https://cmake.org/files/v3.15/cmake-3.15.0-Linux-x86_64.sh  \
&& mkdir /opt/cmake \
&& sh cmake-3.15.0-Linux-x86_64.sh --prefix=/opt/cmake --skip-license \
&& ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake \
&& rm cmake-3.15.0-Linux-x86_64.sh \
&& cmake --version

RUN mkdir ${VCPKG_ROOT} \
 && cd ${VCPKG_ROOT} \
 && git clone https://github.com/microsoft/vcpkg.git . \
 && ./bootstrap-vcpkg.sh \
 && ./vcpkg integrate install \
 && ./vcpkg install gtest

WORKDIR /root/build
ENV PATH="/usr/lib/ccache:${PATH}"
COPY . /opt/orthodox
ENTRYPOINT bash /opt/orthodox/build.sh /root/src