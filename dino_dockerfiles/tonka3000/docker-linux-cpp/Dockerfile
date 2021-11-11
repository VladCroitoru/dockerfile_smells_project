FROM ubuntu:16.04
MAINTAINER tonka3000 <tonka3100@gmail.com>

WORKDIR "/project"

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install build-essential wget python python3 python3-pip cppcheck -y  && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    wget https://cmake.org/files/v3.10/cmake-3.10.2-Linux-x86_64.sh && \
    chmod +x cmake-3.10.2-Linux-x86_64.sh && \
    ./cmake-3.10.2-Linux-x86_64.sh --skip-license --prefix=/usr && \
    rm cmake-3.10.2-Linux-x86_64.sh && \
    wget https://github.com/conan-io/conan/releases/download/1.0.4/conan-ubuntu-64_1_0_4.deb && \
    dpkg -i conan-ubuntu-64_1_0_4.deb && \
    rm conan-ubuntu-64_1_0_4.deb

RUN cmake --version && \
    conan --version && \
    g++ --version