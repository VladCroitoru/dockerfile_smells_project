# FFMPEG Docker File
#
# Version	0.0.1

FROM ubuntu:14.04

MAINTAINER Ned Harris <nedward777@gmail.com>

# Make sure ubuntu is up to date
RUN apt-get update -y

# Install dependancies

RUN apt-get -y install autoconf automake build-essential libass-dev libfreetype6-dev libgpac-dev libsdl1.2-dev libtheora-dev libtool libva-dev libvdpau-dev libvorbis-dev libx11-dev libxext-dev libxfixes-dev pkg-config texi2html zlib1g-dev unzip wget

# Make ffmpeg_sources directory
RUN mkdir ~/ffmpeg_sources

# Install yasm
RUN apt-get -y install yasm

# Install the libx264 library
RUN cd ~/ffmpeg_sources && wget http://download.videolan.org/pub/x264/snapshots/last_x264.tar.bz2 && tar xjvf last_x264.tar.bz2 && cd x264-snapshot* && ./configure --prefix="$HOME/ffmpeg_build" --bindir="$HOME/bin" --enable-static && make && make install && make distclean

# Install the libfdk-aac library
RUN cd ~/ffmpeg_sources && wget -O fdk-aac.zip https://github.com/mstorsjo/fdk-aac/zipball/master && unzip fdk-aac.zip && cd mstorsjo-fdk-aac* && autoreconf -fiv && ./configure --prefix="$HOME/ffmpeg_build" --disable-shared && make && make install && make distclean

# Install libmp3lame MP3 audio encoder
RUN apt-get -y install libmp3lame-dev

# Install libopus Opus audio decoder
RUN apt-get -y install libopus-dev

# Install libvpx VP8/VP9 video encoder and decoder
RUN cd ~/ffmpeg_sources && wget http://webm.googlecode.com/files/libvpx-v1.3.0.tar.bz2 && tar xjvf libvpx-v1.3.0.tar.bz2 && cd libvpx-v1.3.0 && ./configure --prefix="$HOME/ffmpeg_build" --disable-examples && make && make install && make clean

# Install FFMPEG
RUN cd ~/ffmpeg_sources && wget http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 && tar xjvf ffmpeg-snapshot.tar.bz2 --owner root --group root --no-same-owner && cd ffmpeg && PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig" && export PKG_CONFIG_PATH && ./configure --prefix="$HOME/ffmpeg_build" --extra-cflags="-I$HOME/ffmpeg_build/include" --extra-ldflags="-L$HOME/ffmpeg_build/lib" --bindir="$HOME/bin" --extra-libs="-ldl" --enable-gpl --enable-libass --enable-libfdk-aac --enable-libfreetype --enable-libmp3lame --enable-libopus --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-nonfree && make && make install && make distclean && hash -r 

# Setup environment variables
RUN echo "MANPATH_MAP $HOME/bin $HOME/ffmpeg_build/share/man" >> ~/.manpath . ~/.profile



