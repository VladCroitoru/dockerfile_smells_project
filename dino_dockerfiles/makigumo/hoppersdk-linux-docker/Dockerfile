FROM ubuntu:rolling
ENV DEBIAN_FRONTEND noninteractive

#RUN apt-get update -q && apt-get install -qy wget

#RUN echo 'deb http://apt.llvm.org/zesty/ llvm-toolchain-zesty main' > /etc/apt/sources.list.d/llvm.list
#RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add -

RUN apt-get update -q

RUN apt-get install -qy \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libgnutls28-dev \
    libicu-dev \
    libblocksruntime-dev \
    libkqueue-dev \
    libpthread-workqueue-dev \
    clang \
    cmake make git curl \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --quiet --depth 1 https://github.com/makigumo/HopperSDK-v4.git sdk && \
    cd sdk/Linux && \
    ./install.sh

ENV PATH="${PATH}:${HOME}/sdk/Linux/gnustep-Linux-x86_64/bin/"



WORKDIR /data
VOLUME ["/data"]
