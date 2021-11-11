# Defines an image that is used as the base for all FFIG Docker images. This
# includes the dependencies required to build and use FFIG, but not the FFIG
# code or derived applications.

FROM ubuntu:17.10
MAINTAINER FFIG <support@ffig.org>

RUN apt-get -y update && \
    apt-get install -y \
        python-software-properties \
        software-properties-common

# Software dependencies - sorted alphabetically
# Note: Python's pip is used to install CMake following https://blog.kitware.com/cmake-python-wheels/
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test && \
    apt-get -y update && \
    apt-get install -y \
        clang \
        curl \
        dos2unix \
        git \
        golang \
        libc++-dev \
        libc++1 \
        libclang-5.0-dev \
        libunwind8 \
        luajit \
        mono-devel \
        ninja-build \
        pypy \
        python-pip \
        python3 \
        python3-pip \
        ruby \
        ruby-dev


# Install .NET Core
ENV DOTNET_SDK_VERSION 2.0.2
ENV DOTNET_DOWNLOAD_URL https://dotnetcli.blob.core.windows.net/dotnet/Sdk/$DOTNET_SDK_VERSION/dotnet-sdk-$DOTNET_SDK_VERSION-linux-x64.tar.gz

RUN curl -SL $DOTNET_DOWNLOAD_URL --output dotnet.tar.gz \
    && mkdir -p /usr/share/dotnet \
    && tar -zxf dotnet.tar.gz -C /usr/share/dotnet \
    && rm dotnet.tar.gz \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet

# Trigger the population of the local package cache
ENV NUGET_XMLDOC_MODE skip
RUN mkdir warmup \
    && cd warmup \
    && dotnet new \
    && cd .. \
    && rm -rf warmup \
    && rm -rf /tmp/NuGetScratch


# Python dependencies
RUN pip2 install --upgrade pip==9.0.3 cmake && \
    pip2 install jinja2 nose pycodestyle virtualenv && \
    pip3 install --upgrade pip==9.0.3 cmake && \
    pip3 install jinja2 nose pycodestyle virtualenv 

# Ruby dependencies
RUN gem install ffi

# Cleanup
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Rust
# Use recipe from
# https://github.com/rust-lang/docker-rust/blob/e7703b2cf525f2525bdf8d131cd66b5b38b1513c/1.31.0/stretch/Dockerfile
ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:$PATH \
    RUST_VERSION=1.31.0
    
RUN set -eux; \
    dpkgArch="$(dpkg --print-architecture)"; \
    case "${dpkgArch##*-}" in \
        amd64) rustArch='x86_64-unknown-linux-gnu'; rustupSha256='02c0464459b2f88ce99f927b14f6aa4d09c96b9eb6e57808d6c567edce66260a' ;; \
        armhf) rustArch='armv7-unknown-linux-gnueabihf'; rustupSha256='c7a3094b5e81974a5f752c3d6d78f0202e9ee45962140167880a2e0fe5bb3eb7' ;; \
        arm64) rustArch='aarch64-unknown-linux-gnu'; rustupSha256='d1d6ca6c91fa5c22a53f9c7a79dbc49ac2c9056e2d74636e8f091310f157e351' ;; \
        i386) rustArch='i686-unknown-linux-gnu'; rustupSha256='63dd42cdc70b9b026a86d514be4392ab24110ae4537285b5d04e98cdc2cf27d1' ;; \
        *) echo >&2 "unsupported architecture: ${dpkgArch}"; exit 1 ;; \
    esac; \
    url="https://static.rust-lang.org/rustup/archive/1.15.0/${rustArch}/rustup-init"; \
    curl -SL $url --output rustup-init; \
    echo "${rustupSha256} *rustup-init" | sha256sum -c -; \
    chmod +x rustup-init; \
    ./rustup-init -y --no-modify-path --default-toolchain $RUST_VERSION; \
    rm rustup-init; \
    chmod -R a+w $RUSTUP_HOME $CARGO_HOME; \
    rustup --version; \
    cargo --version; \
    rustc --version;

# User and environment setup
RUN useradd ffig && \
    mkdir -p /home/ffig && \
    chown ffig /home/ffig

ENV HOME=/home/ffig \
    LD_LIBRARY_PATH=/usr/lib/llvm-5.0/lib:$LD_LIBRARY_PATH
