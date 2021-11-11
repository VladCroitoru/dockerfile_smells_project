FROM debian:stretch

RUN sed -i "s/stretch main/stretch main contrib non-free/" /etc/apt/sources.list
RUN echo "deb http://www.deb-multimedia.org stretch main non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y --force-yes deb-multimedia-keyring
RUN apt-get update

RUN apt-get install -y \
    autoconf \
    autopoint \
    curl \
    build-essential \
    ffmpeg \
    git \
    libtool \
    libavcodec-dev \
    libavdevice-dev \
    libavformat-dev \
    libavutil-dev \
    libav-tools \
    libjpeg-dev \
    libmicrohttpd-dev \
    libswscale-dev \
    libzip-dev \
    locales \
    wget \
    x264

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

ADD . motion
WORKDIR motion

RUN autoreconf -fiv \
  && ./configure \
  && make \
  && make install
