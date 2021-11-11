FROM debian:unstable-slim

ARG DEBIAN_FRONTEND=noninteractive

# Wait for Debian to ship libwayland-egl
ENV KNOWN_GOOD_MESA=67f7a16b5985
ENV KNOWN_GOOD_CTS=fd68124a565e
ENV KNOWN_GOOD_EPOXY=737b6918703c

ENV GOPATH=/usr/local/go
ENV PATH=$PATH:/usr/local/go/bin
ENV LD_LIBRARY_PATH=/usr/local/lib64:/usr/local/lib
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:/usr/local/lib64/pkgconfig:/usr/local/share/pkgconfig
ENV LDFLAGS="-L/usr/local/lib64"

RUN echo deb-src http://deb.debian.org/debian testing main >> /etc/apt/sources.list
RUN apt-get update && apt-get -y install ca-certificates
RUN apt-get update && apt-get -y install git \
                                         check \
                                         weston \
                                         linux-image-amd64 \
                                         libgbm-dev \
                                         libxvmc-dev \
                                         autoconf \
                                         ccache \
                                         golang-go \
                                         git \
                                         ca-certificates \
                                         procps \
                                         systemd \
                                         dbus \
                                         busybox \
                                         cmake \
                                         spirv-headers \
                                         libsdl2-dev \
                                         strace \
                                         mercurial \
                                         systemd-coredump
RUN apt-get update && apt-get -y build-dep qemu \
                                           mesa \
                                           virglrenderer \
                                           libepoxy \
                                           libsdl2

RUN /usr/sbin/update-ccache-symlinks

RUN go get -v github.com/tomeuv/fakemachine/cmd/fakemachine
RUN go install -x github.com/tomeuv/fakemachine/cmd/fakemachine

# Drop this once http://hg.libsdl.org/SDL/rev/295cf9910d75 makes it into Debian
RUN hg clone http://hg.libsdl.org/SDL
WORKDIR /SDL
RUN ./autogen.sh && \
    ./configure  --prefix=/usr \
                 --includedir=\${prefix}/include \
                 --mandir=\${prefix}/share/man \
                 --infodir=\${prefix}/share/info \
                 --sysconfdir=/etc \
                 --localstatedir=/var \
                 --disable-silent-rules \
                 --libdir=\${prefix}/lib/x86_64-linux-gnu \
                 --libexecdir=\${prefix}/lib/x86_64-linux-gnu \
                 --disable-rpath \
                 --enable-sdl-dlopen \
                 --disable-loadso \
                 --disable-nas \
                 --disable-esd \
                 --disable-arts \
                 --disable-alsa-shared \
                 --disable-pulseaudio-shared \
                 --enable-ibus \
                 --disable-x11-shared \
                 --disable-video-directfb \
                 --enable-video-opengles \
                 --enable-video-wayland \
                 --disable-wayland-shared \
                 --disable-video-vulkan && \
    make -j$(nproc) install && \
    rm -rf /SDL
WORKDIR /

COPY weston.service /usr/lib/systemd/system/.

