FROM ubuntu:14.04
MAINTAINER Benjamin Henrion <zoobab@gmail.com>
LABEL description="A daily build of openwrt trunk for ar71xx arch"

RUN DEBIAN_FRONTEND=noninteractive apt-get update -y -q
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q --force-yes build-essential subversion git-core libncurses5-dev zlib1g-dev gawk flex quilt libssl-dev xsltproc libxml-parser-perl mercurial bzr ecj cvs unzip wget

RUN useradd -d /home/openwrt -m -s /bin/bash openwrt
RUN echo "openwrt ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/openwrt
RUN chmod 0440 /etc/sudoers.d/openwrt

USER openwrt

WORKDIR /home/openwrt
RUN git clone --quiet https://github.com/mirrors/openwrt.git
WORKDIR /home/openwrt/openwrt
RUN echo "CONFIG_TARGET_ar71xx=y" > .config
RUN make defconfig
RUN make prereq
RUN make tools
RUN make toolchain
RUN make
