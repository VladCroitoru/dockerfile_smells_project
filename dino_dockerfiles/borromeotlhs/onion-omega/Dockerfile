# For running a client to bounce off of @ port 9004:
# sudo docker run -d --net=none --expose=[9000] -p 127.0.0.1:9004:9000 -t alljoyn-builder:production
# To connect to this machine after running it

FROM ubuntu

MAINTAINER borromeotlhs@gmail.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -yq 
# list of packages _actually_ needed doesn't include
# python2.7, unzip, wget, gcc-multilib, gettext
RUN apt-get install build-essential subversion libncurses5-dev zlib1g-dev gawk gcc-multilib flex git-core gettext libssl-dev unzip python2.7 wget -yq
# added this to take advantage of caching
RUN apt-get install quilt -yq

RUN git clone git://git.openwrt.org/openwrt.git

WORKDIR openwrt

RUN useradd -m -d /home/onion -p onion onion && adduser onion sudo && chsh -s /bin/bash onion
RUN chown -R onion:onion .

USER onion
RUN cp feeds.conf.default feeds.conf
RUN echo "src-git onion https://github.com/OnionIoT/OpenWRT-Packages.git" >> feeds.conf
#RUN echo "src-git alljoyn git://git.allseenalliance.org/gerrit/core/openwrt_feed;attitude_adjustment" >> feeds.conf

RUN ./scripts/feeds update -a
RUN ./scripts/feeds install python
#RUN ./scripts/feeds install -a -p alljoyn
#RUN ./scripts/feeds install -a -p luci

# This is added as python is needed for node.js gyp formats
USER root
RUN ln -s /usr/bin/python2.7 /usr/bin/python
USER onion

RUN make defconfig
RUN make prereq

ADD appendtoconfig /openwrt/appendtoconfig
RUN cat appendtoconfig/appendtoconfig >> .config
# I expect some warnings from this, but it's a straightforward op
RUN make defconfig
#RUN make
