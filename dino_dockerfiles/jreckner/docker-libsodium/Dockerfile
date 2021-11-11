#
# libsodium Dockerfile
#
#

# Pull base image.
FROM ubuntu:18.04
MAINTAINER Jon Reckner <jreckner@lexmark.com>

# Define Libsodium version
ENV LIBSODIUM_VERSION 1.0.18

# Define workdir
WORKDIR /root

# Install some tools: gcc build tools, unzip, etc
RUN \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install curl build-essential unzip locate

# Download and install libsodium
# https://download.libsodium.org/doc/

# Download & extract & make libsodium
# Move libsodium build
RUN \
    mkdir -p /tmpbuild/libsodium && \
    cd /tmpbuild/libsodium && \
    curl -L https://download.libsodium.org/libsodium/releases/libsodium-${LIBSODIUM_VERSION}.tar.gz -o libsodium-${LIBSODIUM_VERSION}.tar.gz && \
    tar xfvz libsodium-${LIBSODIUM_VERSION}.tar.gz && \
    cd /tmpbuild/libsodium/libsodium-${LIBSODIUM_VERSION}/ && \
    ./configure && \
    make && make check && \
    make install && \
    mv src/libsodium /usr/local/ && \
    rm -Rf /tmpbuild/

# Define default command
CMD ["bash"]

