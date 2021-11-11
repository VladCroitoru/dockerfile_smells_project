
# Ubuntu 20 LTS(Focal Fossa) http://releases.ubuntu.com/focal/
FROM ubuntu:focal

# Use tencent cloud mirror.
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bk
COPY sources.list /etc/apt/sources.list

# https://serverfault.com/questions/949991/how-to-install-tzdata-on-a-ubuntu-docker-image
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

# Install depends for OpenWRT.
RUN apt-get install -y build-essential ccache ecj fastjar file g++ gawk \
    gettext git java-propose-classpath libelf-dev libncurses5-dev \
    libncursesw5-dev libssl-dev python python2.7-dev python3 unzip wget \
    python3-distutils python3-setuptools python3-dev rsync subversion \
    swig time xsltproc zlib1g-dev

# Set mirror to clone code.
ARG MIRROR=https://gitee.com/harvey520

# Clone OpenWRT from gitee mirror.
RUN cd /root && git clone ${MIRROR}/openwrt.git openwrt
RUN cd /root/openwrt && git remote set-url origin https://github.com/openwrt/openwrt.git && git pull

# Cache feeds.
RUN mkdir -p /root/openwrt/feeds
RUN cd /root/openwrt/feeds && git clone ${MIRROR}/packages.git && \
    cd packages && git remote set-url origin https://github.com/openwrt/packages.git && git pull
RUN cd /root/openwrt/feeds && git clone ${MIRROR}/luci.git && \
    cd luci && git remote set-url origin https://github.com/openwrt/luci.git && git pull
RUN cd /root/openwrt/feeds && git clone ${MIRROR}/routing.git && \
    cd routing && git remote set-url origin https://github.com/openwrt/routing.git && git pull
RUN cd /root/openwrt/feeds && git clone ${MIRROR}/telephony.git && \
    cd telephony && git remote set-url origin https://github.com/openwrt/telephony.git && git pull

# Use stable branch for feeds.
ARG BRANCH=openwrt-21.02
RUN cd /root/openwrt && git checkout ${BRANCH} && \
    cd /root/openwrt/feeds/packages && git checkout ${BRANCH} && \
    cd /root/openwrt/feeds/luci && git checkout ${BRANCH} && \
    cd /root/openwrt/feeds/routing && git checkout ${BRANCH} && \
    cd /root/openwrt/feeds/telephony && git checkout ${BRANCH}
# Create the tmp file for feeds.
RUN cd /root/openwrt/feeds/packages && mkdir -p packages.tmp && echo "https://github.com/openwrt/packages.git;${BRANCH}" > packages.tmp/location && \
    cd /root/openwrt/feeds/luci && mkdir -p luci.tmp && echo "https://github.com/openwrt/luci.git;${BRANCH}" > luci.tmp/location && \
    cd /root/openwrt/feeds/routing && mkdir -p routing.tmp && echo "https://github.com/openwrt/routing.git;${BRANCH}" > routing.tmp/location && \
    cd /root/openwrt/feeds/telephony && mkdir -p telephony.tmp && echo "https://github.com/openwrt/telephony.git;${BRANCH}" > telephony.tmp/location

# Update feeds.
RUN cd /root/openwrt && ./scripts/feeds update -a && ./scripts/feeds install -a

# Install dev packages.
RUN apt-get install -y pkg-config vim

# For docker to use root to build OpenWRT.
ENV FORCE_UNSAFE_CONFIGURE 1

# Setup the workdir.
WORKDIR /root/openwrt
