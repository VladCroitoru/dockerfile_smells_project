FROM ubuntu:18.04
MAINTAINER https://github.com/tinytux

ENV HOME /root

RUN apt-get update && \
    apt-get install -y \
        wget \
        xz-utils lzma \
        make gcc libelf-dev bc \
        bison build-essential flex gperf libasound2-dev \
        libatkmm-1.6-dev libbz2-dev libcap-dev libcups2-dev libdrm-dev libegl1-mesa-dev libfontconfig1-dev \
        libfreetype6-dev libgcrypt11-dev libglu1-mesa-dev libicu-dev libnss3-dev \
        libpci-dev libpulse-dev libudev-dev libx11-dev libx11-xcb-dev libxcb-composite0 \
        libxcb-composite0-dev libxcb-cursor-dev libxcb-cursor0 libxcb-damage0 libxcb-damage0-dev libxcb-dpms0 \
        libxcb-dpms0-dev libxcb-dri2-0 libxcb-dri2-0-dev libxcb-dri3-0 libxcb-dri3-dev libxcb-ewmh-dev \
        libxcb-ewmh2 libxcb-glx0 libxcb-glx0-dev libxcb-icccm4 libxcb-icccm4-dev libxcb-image0 \
        libxcb-image0-dev libxcb-keysyms1 libxcb-keysyms1-dev libxcb-present-dev libxcb-present0 \
        libxcb-randr0 libxcb-randr0-dev libxcb-record0 libxcb-record0-dev libxcb-render-util0 \
        libxcb-render-util0-dev libxcb-render0 libxcb-render0-dev libxcb-res0 libxcb-res0-dev \
        libxcb-screensaver0 libxcb-screensaver0-dev libxcb-shape0 libxcb-shape0-dev libxcb-shm0 \
        libxcb-shm0-dev libxcb-sync-dev libxcb-sync1 libxcb-util-dev libxcb-util0-dev \
        libxcb-util1 libxcb-xf86dri0 libxcb-xf86dri0-dev libxcb-xfixes0 \
        libxcb-xfixes0-dev libxcb-xinerama0 libxcb-xinerama0-dev libxcb-xkb-dev libxcb-xkb1 \
        libxcb-xtest0 libxcb-xtest0-dev libxcb-xv0 libxcb-xv0-dev libxcb-xvmc0 libxcb-xvmc0-dev \
        libxcb1 libxcb1-dev libxcomposite-dev libxcursor-dev libxdamage-dev libxext-dev libxfixes-dev libxi-dev \
        libxrandr-dev libxrender-dev libxss-dev libxtst-dev perl python ruby \
        libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev x11proto-print-dev libxslt1-dev libssl1.0-dev

RUN groupadd -g 1000 user && useradd --no-log-init -r -g 1000 -u 1000 user && mkdir /home/user && chown user:user /home/user

USER user
RUN cd /home/user && \
    wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.14.43.tar.xz

RUN cd /home/user && \
    wget http://download.qt.io/official_releases/qt/5.9/5.9.5/single/qt-everywhere-opensource-src-5.9.5.tar.xz

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
#CMD ["su", "-", "user", "-c", "/docker-entrypoint.sh"]

USER root
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
