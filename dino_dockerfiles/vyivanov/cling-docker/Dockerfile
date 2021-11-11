FROM ubuntu
MAINTAINER inbox@vova-ivanov.info

RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    python \
    groff \
    wget
    
WORKDIR /opt    
    
RUN git clone http://root.cern.ch/git/llvm.git && \
    cd llvm && \
    git checkout cling-patches && \
    cd tools && \
    git clone http://root.cern.ch/git/cling.git && \
    git clone http://root.cern.ch/git/clang.git && \
    cd clang && \
    git checkout cling-patches
    
RUN mkdir build && \
    cd build && \
    ../llvm/configure --prefix=/usr/local && \
    make && \
    make install

RUN rm -rf build && rm -rf llvm

ENTRYPOINT ["cling"]
