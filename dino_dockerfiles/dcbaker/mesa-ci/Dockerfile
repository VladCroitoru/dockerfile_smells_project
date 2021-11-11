FROM debian:testing
MAINTAINER Dylan Baker <dylan@pnwbakers.com>

RUN apt-get update -qq && apt-get install -qq -y \
        locales \
        build-essential \
        libelf-dev \
        llvm-3.9-dev \
        llvm-4.0-dev \
        llvm-5.0-dev \
        ninja-build \
        pkg-config \
        python \
        python-mako \
        python3-pip \
        scons \
        wget \
        zlib1g-dev \
        xz-utils \
        libexpat1-dev \
        libx11-xcb-dev \
        libxdamage-dev \
        libxfixes-dev \
        libxext-dev \
        libxml2-dev

RUN locale-gen C.UTF-8 && /usr/sbin/update-locale LANG=C.UTF-8

ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

RUN pip3 install meson

RUN wget https://xorg.freedesktop.org/releases/individual/util/util-macros-1.19.0.tar.bz2
RUN tar -xf util-macros-1.19.0.tar.bz2
RUN cd util-macros-1.19.0 && ./configure --prefix=/usr && make install

RUN wget https://xorg.freedesktop.org/releases/individual/proto/glproto-1.4.17.tar.bz2
RUN tar -xf glproto-1.4.17.tar.bz2
RUN cd glproto-1.4.17 && ./configure --prefix=/usr && make install

RUN wget https://xorg.freedesktop.org/releases/individual/proto/dri2proto-2.8.tar.bz2
RUN tar -xf dri2proto-2.8.tar.bz2
RUN cd dri2proto-2.8 && ./configure --prefix=/usr && make install

RUN wget https://xcb.freedesktop.org/dist/xcb-proto-1.11.tar.bz2
RUN tar -xf xcb-proto-1.11.tar.bz2
RUN cd xcb-proto-1.11 && ./configure --prefix=/usr && make install

RUN wget https://xcb.freedesktop.org/dist/libxcb-1.11.tar.bz2
RUN tar -xf libxcb-1.11.tar.bz2
RUN cd libxcb-1.11 && ./configure --prefix=/usr && make install

RUN wget https://xorg.freedesktop.org/releases/individual/lib/libpciaccess-0.13.4.tar.bz2
RUN tar -xf libpciaccess-0.13.4.tar.bz2
RUN cd libpciaccess-0.13.4 && ./configure --prefix=/usr && make install

RUN wget https://dri.freedesktop.org/libdrm/libdrm-2.4.82.tar.bz2
RUN tar -xf libdrm-2.4.82.tar.bz2
RUN cd libdrm-2.4.82 && ./configure --prefix=/usr && make install

RUN wget https://xorg.freedesktop.org/releases/individual/lib/libxshmfence-1.2.tar.bz2
RUN tar -xf libxshmfence-1.2.tar.bz2
RUN cd libxshmfence-1.2 && ./configure --prefix=/usr && make install

RUN wget https://people.freedesktop.org/~aplattner/vdpau/libvdpau-1.1.tar.bz2
RUN tar -xf libvdpau-1.1.tar.bz2
RUN cd libvdpau-1.1 && ./configure --prefix=/usr && make install

RUN wget https://www.freedesktop.org/software/vaapi/releases/libva/libva-1.6.2.tar.bz2
RUN tar -xf libva-1.6.2.tar.bz2
RUN cd libva-1.6.2 && ./configure --prefix=/usr --disable-wayland --disable-dummy-driver && make install

RUN wget https://wayland.freedesktop.org/releases/wayland-1.11.1.tar.xz
RUN tar -xf wayland-1.11.1.tar.xz
RUN cd wayland-1.11.1 && ./configure --prefix=/usr --disable-documentation && make install

RUN wget https://wayland.freedesktop.org/releases/wayland-protocols-1.8.tar.xz
RUN tar -xf wayland-protocols-1.8.tar.xz
RUN cd wayland-protocols-1.8 && ./configure --prefix=/usr && make install
