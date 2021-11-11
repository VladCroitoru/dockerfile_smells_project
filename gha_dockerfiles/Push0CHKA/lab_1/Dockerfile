# rusdevops/bootstrap-cpp image
FROM ubuntu:20.04
LABEL maintainer="rusdevops@gmail.com"
ENV DEBIAN_FRONTEND noninteractive
RUN apt -y update && \
    apt -y install software-properties-common doxygen rpm g++-7 curl llvm g++ lcov gcovr cmake python3-pip clang git && \
    add-apt-repository -y ppa:ubuntu-toolchain-r/test && \
    pip3 install cpplint gitpython requests && \
    apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
