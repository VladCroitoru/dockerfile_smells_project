FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y

RUN apt-get install -y --no-install-recommends \
    bc \
    bison \
    ca-certificates \
    clang \
    cmake \
    curl \
    file \
    flex \
    gcc \
    g++ \
    git \
    libelf-dev \
    libssl-dev \
    lld \
    make \
    ninja-build \
    python3 \
    texinfo \
    xz-utils \
    zlib1g-dev \
    patchelf

COPY . /work

VOLUME /work/llvm-project /work/install

ENTRYPOINT ["/work/build-toolchain.sh"]
