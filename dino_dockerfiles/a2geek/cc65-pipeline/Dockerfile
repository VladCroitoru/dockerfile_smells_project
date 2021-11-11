FROM alpine:latest

LABEL description="This is a cc65 Docker container intended to be used for build pipelines."

ENV BUILD_DIR="/tmp" \
    CC65_VERSION="V2.17" \
    NULIB2_VERSION="v3.1.0" \
    AC_RELEASE="v1-4-0" \
    AC_VERSION="1.4.0"

COPY bin /usr/local/bin

RUN apk add --no-cache build-base && \
    echo "Building CC65 ${CC65_VERSION}" && \
    cd ${BUILD_DIR} && \
    wget https://github.com/cc65/cc65/archive/${CC65_VERSION}.tar.gz && \
    tar xzf ${CC65_VERSION}.tar.gz && \
    cd cc65* && \
    env PREFIX=/usr/local make && \
    env PREFIX=/usr/local make install && \
    echo "Building NuLib2 ${NULIB2_VERSION}" && \
    cd ${BUILD_DIR} && \
    wget https://github.com/fadden/nulib2/archive/${NULIB2_VERSION}.tar.gz && \
    tar xzf ${NULIB2_VERSION}.tar.gz && \
    cd nulib2* && \
    cd nufxlib && \
    ./configure && \
    make && \
    make install && \
    cd ../nulib2 && \
    ./configure && \
    make && \
    make install && \
    echo "Adding AppleCommander" && \
    wget https://github.com/AppleCommander/AppleCommander/releases/download/${AC_RELEASE}/AppleCommander-ac-${AC_VERSION}.jar && \
    mkdir -p /usr/local/share/java && \
    mv AppleCommander-ac-${AC_VERSION}.jar /usr/local/share/java/AppleCommander-ac.jar && \
    echo "Cleaning up" && \
    cd ${BUILD_DIR} && \
    rm -rf * && \
    apk del --no-cache build-base && \
    echo "Adding other required build-tools exclusive of other C compilers!" && \
    apk add --no-cache make openjdk8-jre && \
    chmod +x /usr/local/bin/*
