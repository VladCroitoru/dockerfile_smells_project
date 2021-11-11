FROM quantumobject/docker-baseimage

RUN sed 's/main$/main universe multiverse/' -i /etc/apt/sources.list

# get dependencies
# ref: https://github.com/jrottenberg/ffmpeg/blob/master/run.sh
# ref: https://github.com/sameersbn/docker-ffmpeg/blob/master/install.sh
# ref: https://github.com/cellofellow/ffmpeg/blob/master/script/build.sh

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \
    g++ git mercurial subversion curl wget \
    yasm autoconf automake build-essential cmake libtool pkg-config texi2html zlib1g-dev \
    libass-dev libgpac-dev libtheora-dev libvdpau-dev libvorbis-dev libmp3lame-dev \
    libmpeg2-4-dev libfaad-dev libmpg123-dev libmad0-dev libvo-aacenc-dev libogg-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# from source libxvidcore-dev

ADD build.sh /build.sh
RUN /bin/bash /build.sh
ENV LD_LIBRARY_PATH /usr/local/lib

CMD ["/sbin/my_init"]
