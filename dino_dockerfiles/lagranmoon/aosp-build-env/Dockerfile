FROM ubuntu:14.04
# RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list\
#     && apt update \ 
    # && apt install -y wget \
    # && wget https://mirrors.ustc.edu.cn/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jre-headless_8u45-b14-1_amd64.deb \
    #         https://mirrors.ustc.edu.cn/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jre_8u45-b14-1_amd64.deb \
    #         https://mirrors.ustc.edu.cn/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jdk_8u45-b14-1_amd64.deb \
    # && dpkg -i *.deb || apt -f -y install \
RUN apt update\
    && dpkg --add-architecture i386 && apt update \
    && apt install -y lib32z1 lib32ncurses5 lib32bz2-1.0 \
    && apt install -y git-core gnupg flex bison gperf build-essential zip curl zlib1g-dev gcc-multilib \
                      g++-multilib libc6-dev-i386 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev \
                      ccache libgl1-mesa-dev libxml2-utils xsltproc unzip python-networkx libnss-sss:i386 
    # && rm -rf *.deb
