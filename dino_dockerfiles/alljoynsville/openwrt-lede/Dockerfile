FROM ubuntu:xenial

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yqq sudo git-core subversion build-essential gcc-multilib ccache quilt \
                       libncurses5-dev zlib1g-dev gawk flex gettext wget unzip python vim libssl-dev && \
    apt-get clean && \
    useradd -m openwrt && \
    echo 'openwrt ALL=NOPASSWD: ALL' > /etc/sudoers.d/openwrt
USER openwrt
RUN cd /home/openwrt && \
    git clone --depth 1 --branch v17.01.4 https://git.lede-project.org/source.git openwrt && \
    cd openwrt && \
    ./scripts/feeds update && \
    rm -rf tmp
WORKDIR /home/openwrt/openwrt
