FROM ubuntu:vivid

MAINTAINER ACUVE sub_chon@yahoo.co.jp

# Set Locale

RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8



# Enable Universe and Multiverse and install dependencies.

RUN echo deb http://archive.ubuntu.com/ubuntu precise universe multiverse >> /etc/apt/sources.list; apt-get update; apt-get -y install autoconf automake build-essential git mercurial cmake libass-dev libgpac-dev libtheora-dev libogg-dev libvorbis-dev libmp3lame-dev flac libflac-dev libtool libvdpau-dev pkg-config texi2html zlib1g-dev wget yasm libfreetype6-dev mkvtoolnix python3-dev python3-pip python3-sphinx fftw3-dev nasm; apt-get clean; pip3 install cython

# Run build script

ADD script/* /
RUN ["/bin/bash", "/build.sh"]

CMD ["/bin/bash"]
