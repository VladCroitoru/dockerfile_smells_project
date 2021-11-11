FROM golang:1.3-onbuild

MAINTAINER skrassiev <bg2128506@gmail.com>

#from https://github.com/ozzyjohnson/docker-ffmpeg-webm/blob/master/Dockerfile

# Update and install minimal.
RUN \
  apt-get update \
            --quiet \
  && apt-get install sox \
            --yes \
  && apt-get install \ 
            --yes \
            --no-install-recommends \
            --no-install-suggests \
        autoconf \
        automake \
        build-essential \
        ca-certificates \
        git-core \
        libass-dev \
        libgpac-dev \
        libtheora-dev \
        libtool \
        libvorbis-dev \
        pkg-config \
        python-minimal \
        texi2html \
        zlib1g-dev \

# Clean up packages.
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Prepare for cloning/building.
WORKDIR /tmp

## Yasm
RUN git clone git://github.com/yasm/yasm.git \
    && cd yasm \
    && ./autogen.sh \
    && ./configure \
    && make -j`getconf _NPROCESSORS_ONLN` \
    && make install \
    && make distclean \
    && cd /tmp \
    && rm -rf /tmp/yasm

## x264
RUN git clone git://git.videolan.org/x264.git \
    && cd x264 \
    && ./configure --enable-static --disable-opencl \
    && make -j`getconf _NPROCESSORS_ONLN` \
    && make install \
    && make distclean \
    && cd /tmp \
    && rm -rf /tmp/x264

## libopus
RUN git clone git://git.opus-codec.org/opus.git \
    && cd opus \
    && ./autogen.sh \
    && ./configure --disable-shared \
    && make -j`getconf _NPROCESSORS_ONLN` \
    && make install \
    && make distclean \
    && cd /tmp \
    && rm -rf /tmp/opus

## libvpx
RUN git clone https://chromium.googlesource.com/webm/libvpx \
    && cd libvpx \
    && ./configure --disable-shared \
    && make -j`getconf _NPROCESSORS_ONLN` \
    && make install \
    && make clean \
    && cd /tmp \
    && rm -rf /tmp/libvpx

## ffmpeg
RUN git clone git://source.ffmpeg.org/ffmpeg.git \
    && cd ffmpeg \
    && ./configure \
        --disable-debug \
        --enable-small \
        --extra-libs=-ldl \
        --enable-gpl \
        --enable-libass \
        --enable-libopus \
        --enable-libtheora \
        --enable-libvorbis \
        --enable-libvpx \
        --enable-libx264 \
    && make -j`getconf _NPROCESSORS_ONLN` \
    && make install \
    && make distclean \
    && cd /tmp \
    && rm -rf /tmp/ffmpeg

# A volume for video output.
ONBUILD VOLUME ["/data"]

# Prepare to run.
WORKDIR /data

