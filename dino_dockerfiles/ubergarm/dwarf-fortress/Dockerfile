FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

# install NVIDIA CUDA 384 to match host machine's exact version
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
            software-properties-common

RUN add-apt-repository ppa:graphics-drivers/ppa

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
            nvidia-384

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
            default-jre \
            libsdl1.2debian \
            libsdl-image1.2 \
            libsdl-ttf2.0-0 \
            libgtk2.0-0 \
            libopenal1 \
            libjpeg62 \
            libglu1-mesa \
            libqt5core5a \
            libqt5widgets5 \
            libqt5qml5 \
            openssl \
            wget \
            coreutils \
            qtchooser \
            libqt5script5 \
            libqt5scripttools5 \
            libqxt-core0 \
            libqxt-gui0 \
            xterm \
    && rm -rf /var/lib/apt/lists/*

# ADD LinuxLNP-0.44.09-r01.tar.gz /df/
RUN mkdir -p /df && \
    cd /df && \
    wget -O /df/LinuxLNP-0.44.09-r01.tar.gz "http://dffd.bay12games.com/download.php?id=13244&f=LinuxLNP-0.44.09-r01.tar.gz" && \
    echo "4799c4a1550e0b5edc5509a3e96c2b14baae52bef6c9f6e25d8fc3a4e39fc14c  LinuxLNP-0.44.09-r01.tar.gz" | sha256sum -c - && \
    tar -xf /df/LinuxLNP-0.44.09-r01.tar.gz && \
    rm -f /df/LinuxLNP-0.44.09-r01.tar.gz

WORKDIR /df/LinuxLNP-0.44.09-r01

CMD /bin/bash
