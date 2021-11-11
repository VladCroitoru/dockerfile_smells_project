# Docker container for doing test builds
FROM debian
MAINTAINER Ralph Giles <giles@thaumas.net>

# Update system
RUN apt-get -qq update
RUN apt-get -qq upgrade

# Install development tools
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -qqy install git gcc make
RUN apt-get -qqy install automake autoconf libtool

# Download
RUN git clone https://git.xiph.org/opus.git

# Now update and build whenever the image is launched
CMD cd opus && git pull && ./autogen.sh && ./configure && make -j4 check
