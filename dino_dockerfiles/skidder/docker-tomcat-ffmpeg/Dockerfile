FROM tomcat:7.0.75-jre8

MAINTAINER Scott Kidder <kidder.scott@gmail.com>

# Enable Universe and Multiverse and install dependencies.
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe multiverse >> /etc/apt/sources.list; apt-get update; apt-get -y --fix-missing install autoconf automake build-essential git mercurial cmake libass-dev libgpac-dev libtheora-dev libtool libvdpau-dev libvorbis-dev pkg-config texi2html zlib1g-dev libmp3lame-dev wget yasm; apt-get clean

# Run build script
ADD script/build.sh /build.sh
RUN ["/bin/bash", "/build.sh"]
