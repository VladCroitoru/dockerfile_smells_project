# linux dev environment for LEDE project 
FROM ubuntu:14.04

MAINTAINER borromeotlhs@gmail.com

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install subversion g++ zlib1g-dev build-essential git python \
libncurses5-dev gawk gettext unzip file libssl-dev wget -y

# Thanks to @werecatf for this work on omega2plus
RUN git clone https://github.com/lede-project/source.git lede-17.01

RUN adduser omega

RUN chown -R omega:omega lede
WORKDIR lede
USER omega

RUN ./scripts/feeds update -a
RUN ./scripts/feeds install -a

RUN make defconfig
# these are the following commands I ran in order to make this image
# choose RALINK MT7688 for onion omega2plus
#RUN make menuconfig
#RUN make -j1 V=s
