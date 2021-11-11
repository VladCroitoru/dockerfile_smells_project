FROM ubuntu:19.04
MAINTAINER sebastian.breuers@elfin.de

RUN apt-get update && apt-get install -y \
        automake \
        busybox \
        cmake \
        curl \
        g++ \
        git \
        jq \
        lcov \
        libblkid-dev \
        libboost-all-dev \
        libcgicc-dev \
        libcurl4-gnutls-dev \
        libdbus-1-dev\
        libgpgme11-dev \
        libi2c-dev \
        libjsoncpp-dev \
        libpcre3-dev \
        libqt5svg5-dev \
        libssl-dev \
        libsystemd-dev \
        libtar-dev \
        libtool \
        libtool-bin \
        make \
        openssl \
        pkg-config \
        tar \
        unzip \
        wget \
        autorevision \
        qt5-default \
        qtdeclarative5-dev \
        libmediainfo-dev \
        qtbase5-private-dev \
        libarchive-dev \
        libfontconfig1-dev \
        libglib2.0-dev \
        libfreetype6-dev \
        libxrender-dev \
        libudev-dev \
        libmtdev-dev \
        && apt-get clean;

RUN git clone https://github.com/google/googletest.git googletest \
        && cd googletest \
        && cmake -DBUILD_GMOCK=ON -DCMAKE_INSTALL_PREFIX=/usr/ ./CMakeLists.txt && make && make install \
        && cd -;

RUN mkdir -p /usr/lib/x86_64-linux-gnu \
        && ln -s libboost_thread.so /usr/lib/x86_64-linux-gnu/libboost_thread-mt.so;

RUN git clone https://github.com/elfin-sbreuers/mqtt_cpp.git \
        && mkdir mqtt_cpp/build \
        && cd mqtt_cpp/build \
        && cmake -DMQTT_NO_TLS=OFF -DMQTT_BUILD_EXAMPLES=OFF -DMQTT_BUILD_TESTS=OFF .. \
        && make install
RUN wget https://github.com/kergoth/tslib/releases/download/1.1/tslib-1.1.tar.xz \
    && tar xf tslib-1.1.tar.xz \
    && cd tslib-1.1 \
    && ./autogen.sh \
    && ./configure --enable-shared --disable-h3600 --enable-input --disable-corgi --disable-collie --disable-mk712 --disable-arctic2 --disable-ucb1x00 \
    && make \
    && make install \
    && cd -

COPY files/bump_patch_version /usr/local/bin/bump_patch_version

RUN wget https://github.com/ChaiScript/ChaiScript/archive/v6.1.0.tar.gz -O chaiscript.tar.gz \
        && tar xzvf chaiscript.tar.gz \
        && cd ChaiScript-6.1.0/ \
        && mkdir build \
        && cd build/ \
        && cmake -DBUILD_TESTING=OFF .. \
        && make -j3 \
        && make install \
        && cd ../.. \
        && rm -r ChaiScript-6.1.0/

RUN export version=3.9.0; export archive=protobuf-cpp-${version}.tar.gz; \
        curl -L https://github.com/protocolbuffers/protobuf/releases/download/v${version}/${archive} -o ${archive} \
        && tar -xf ${archive} \
        && cd protobuf-${version} \
        && mkdir build \
        && cd build \
        && ../configure \
        && make \
        && make install \
        && ldconfig \
        && cd ../.. \
        && rm -r protobuf-${version}
