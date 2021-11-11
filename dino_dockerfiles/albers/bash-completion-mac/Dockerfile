FROM ubuntu:14.04
MAINTAINER Harald Albers

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
        bison \
        ca-certificates \
        g++ \
        make \
        wget && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*

ENV LEGACY_BASH_VERSION 3.2.57
ENV BUILD_DIR /tmp/bash-$LEGACY_BASH_VERSION
RUN wget -O- -q https://ftp.gnu.org/gnu/bash/bash-${LEGACY_BASH_VERSION}.tar.gz | tar xzf - -C /tmp && \
    cd $BUILD_DIR && \
    ./configure --exec-prefix= && \
    make && \
    make install && \
    cd .. && \
    rm -r $BUILD_DIR

ENV LEGACY_COMPLETION_VERSION 1.3
ENV BUILD_DIR /tmp/bash-completion-$LEGACY_COMPLETION_VERSION
RUN wget -O- -q https://bash-completion.alioth.debian.org/files/bash-completion-${LEGACY_COMPLETION_VERSION}.tar.bz2 | tar xjf - -C /tmp && \
    cd $BUILD_DIR && \
    ./configure --prefix= && \
    make && \
    make install && \
    cd .. && \
    rm -r $BUILD_DIR

RUN echo ". /etc/bash_completion" >> /root/.bashrc
RUN echo "shopt -u extglob" >> /root/.bashrc

WORKDIR /root
CMD /bin/bash
