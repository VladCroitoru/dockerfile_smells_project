FROM kz8s/yocto
MAINTAINER jono <jono@bowerswilkins.com>

ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN set -eux &&\
    apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -yq \
        autoconf clang cmake fontconfig gdb graphviz libcairo2-dev libfreetype6-dev \
        libgbm-dev libgl1-mesa-dri libgles1-mesa-dev libgles2-mesa-dev \
        libjpeg62-turbo-dev liblua5.1-0-dev libpango1.0-dev libsqlite3-dev python3-dev uuid-dev &&\
    rm -rf /var/lib/apt-lists/*

WORKDIR /src

RUN set -eux &&\
    git clone https://github.com/jmmv/atf &&\
    git clone https://github.com/jmmv/lutok &&\
    git clone https://github.com/jmmv/kyua &&\
    git clone https://github.com/google/protobuf &&\
    git clone https://github.com/dropbox/json11 
    
COPY *.patch /src/lutok/

ENV CC=clang
ENV CXX=clang++

RUN set -eux &&\
    cd atf &&\
    autoreconf -i -s -I/usr/share/aclocal &&\
    ./configure --prefix=/usr &&\
    make &&\
    make install clean

RUN set -eux &&\
    cd lutok &&\
    patch configure.ac 0001-set-WITH_ATF-false.patch &&\
    patch configure.ac 0002-don-t-check-for-ATF.patch &&\
    autoreconf -i -s -I/usr/share/aclocal &&\
    ./configure --prefix=/usr &&\
    make &&\
    make install clean

RUN set -eux &&\
    cd kyua &&\
    autoreconf -i -s &&\
    ./configure --prefix=/usr &&\
    make &&\
    make install clean
    
RUN set -eux &&\
    cd protobuf &&\
    ./autogen.sh &&\
    ./configure &&\
    make &&\
    make install clean

RUN set -eux &&\
    cd json11 &&\
    cmake -D CMAKE_CXX_FLAGS=-std=c++11 . &&\
    make &&\
    make install clean &&\
    mkdir -p /usr/include/json11 &&\
    mv /usr/include/x86_64-linux-gnu/json11.hpp /usr/include/json11/

    

CMD [ "/bin/bash" ]
