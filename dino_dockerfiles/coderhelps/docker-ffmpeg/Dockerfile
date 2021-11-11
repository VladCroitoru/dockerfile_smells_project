FROM centos:7

RUN yum install -y autoconf automake bzip2 cmake freetype-devel gcc gcc-c++ git libtool make mercurial nasm pkgconfig zlib-devel which

WORKDIR /ffmpeg

COPY build-ffmpeg.sh /ffmpeg/

RUN /ffmpeg/build-ffmpeg.sh

cmd ["ffmpeg", "--help"]
