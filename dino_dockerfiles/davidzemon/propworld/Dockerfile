FROM ubuntu:19.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
apt-get install --yes \
    wget \
    git \
    build-essential \
    cmake \
    cmake-curses-gui \
    vim \
    sudo \
    xutils

# PropGCC
ENV PROPGCC_PREFIX=/opt/parallax.gcc4_1.9.0
RUN wget "https://ci.zemon.name/repository/download/PropGCC5_Gcc4linuxX64/3620:id/propellergcc-alpha_v1_9_0-gcc4-linux-x64.tar.gz?guest=1" \
       --quiet \
       -O /tmp/propgcc4.tar.gz && \
    tar -xf /tmp/propgcc4.tar.gz --directory /tmp && \
    mv /tmp/parallax ${PROPGCC_PREFIX} && \
    rm /tmp/propgcc4.tar.gz

# PropWare
RUN wget "https://ci.zemon.name/repository/download/PropWare_Develop/3630:id/propware_3.0.0.221-1_all.deb?guest=1" \
        --quiet \
        -O /tmp/propware.deb && \
    dpkg -i /tmp/propware.deb && \
    rm /tmp/propware.deb

# SimpleIDE
RUN wget "https://ci.zemon.name/repository/download/SimpleIDE_Qt5side/1677:id/SimpleIDE-1.1.1.x86_64.linux.tar.bz2?guest=1" \
        --quiet \
        -O /tmp/simpleide.tar.bz2 && \
    tar -xf /tmp/simpleide.tar.bz2 -C /tmp && \
    cd /tmp/SimpleIDE-1.1.1 && \
    ./setup.sh install && \
    cd / && \
    rm -rf /tmp/simpleide.tar.gz /tmp/SimpleIDE-1.1.1

# PropellerIDE
RUN wget "https://www.parallax.com/sites/default/files/downloads/propelleride-0.33.3-amd64.deb" \
        --quiet \
        -O /tmp/propelleride.deb && \
    dpkg -i /tmp/propelleride.deb ; \
    apt-get install --fix-broken --yes && \
    rm /tmp/propelleride.deb

# PropLoader
RUN wget "https://ci.zemon.name/repository/download/PropLoader_LinuxX64/3598:id/proploader.tar.gz?guest=1" \
        --quiet \
        -O /tmp/proploader.tar.gz && \
    tar -xf /tmp/proploader.tar.gz -C /usr/local/bin && \
    rm /tmp/proploader.tar.gz

# Spin2Cpp
RUN wget "https://ci.zemon.name/repository/download/Spin2Cpp_Linux/3600:id/spin2cpp.tar.gz?guest=1" \
        --quiet \
        -O /tmp/spin2cpp.tar.gz && \
    tar -xf /tmp/spin2cpp.tar.gz -C /usr/local/bin && \
    rm /tmp/spin2cpp.tar.gz

# OpenSpin
RUN wget "https://ci.zemon.name/repository/download/OpenSpin_LinuxX8664/2555:id/openspin.tar.gz?guest=1" \
        --quiet \
        -O /tmp/openspin.tar.gz && \
    tar -xf /tmp/openspin.tar.gz -C /usr/local/bin && \
    rm /tmp/openspin.tar.gz

COPY bst.linux /usr/local/bin/bst.linux
COPY bstc.linux /usr/local/bin/bstc.linux
