FROM ubuntu:16.04
MAINTAINER eclark@apache.org
RUN apt-get -qq update && \
    apt-get install -y wget software-properties-common && \
    wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \
    apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial main" && \
    add-apt-repository ppa:ubuntu-toolchain-r/test && \
    apt-get -qq update && \
    apt-get install -y gdb gdbserver build-essential valgrind vim git net-tools clang-3.9 lldb-3.9 gcc-5 g++-5 gcc-6 g++-6 libcurl3-openssl-dev strace upx && \
    apt-get -qq clean && \
    apt-get -y -qq autoremove && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/ && \
    mkdir -p /var/lib/{apt,dpkg,cache,log}/ && \
    rm -rf /tmp/*

RUN   mkdir -p /usr/local/src/ && cd /usr/local/src/ && \
      git clone https://github.com/radare/radare2.git && \
      cd radare2 && \
      ./sys/install.sh && \
      make symstall

WORKDIR /opt/share/
EXPOSE 9090
