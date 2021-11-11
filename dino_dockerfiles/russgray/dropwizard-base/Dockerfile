FROM openjdk:8-jdk

RUN \
    apt-get update && \
    apt-get -y install curl binutils gcc autoconf make unzip

ENV LIBSODIUM_VERSION 1.0.16
ENV GLOWROOT_VERSION 0.10.5

# build libsodium
RUN \
    mkdir -p /tmpbuild/libsodium && \
    cd /tmpbuild/libsodium && \
    curl -L -s https://download.libsodium.org/libsodium/releases/libsodium-$LIBSODIUM_VERSION.tar.gz -o libsodium-$LIBSODIUM_VERSION.tar.gz && \
    tar xfvz libsodium-$LIBSODIUM_VERSION.tar.gz && \
    cd /tmpbuild/libsodium/libsodium-$LIBSODIUM_VERSION/ && \
    ./configure && \
    make && make check && \
    make install

# grab glowroot and put it in a known place
RUN \
    mkdir -p /tmpbuild/glowroot && \
    cd /tmpbuild/glowroot && \
    curl -L -s https://github.com/glowroot/glowroot/releases/download/v$GLOWROOT_VERSION/glowroot-$GLOWROOT_VERSION-dist.zip -o glowroot-$GLOWROOT_VERSION-dist.zip && \
    unzip glowroot-$GLOWROOT_VERSION-dist.zip -d /opt

# clean up
RUN \
    apt-get -y remove curl binutils gcc autoconf make unzip && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    rm -Rf /tmpbuild/
