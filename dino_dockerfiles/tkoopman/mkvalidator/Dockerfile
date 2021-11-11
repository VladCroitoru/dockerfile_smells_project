FROM ubuntu:latest
LABEL maintainer "T Koopman"

RUN \
  apt-get update && \
  apt-get install -y \
            mkvtoolnix \
            ffmpeg \
            build-essential \
            checkinstall \
            lib32ncurses5 \
            lib32z1 \
            gcc-multilib \
            g++-multilib \
            libxxf86vm-dev \
            libglu1-mesa-dev \
            libxft-dev \
            wget \
            nano && \
  cd /root && \
  wget -O mkclean-0.8.7.tar.bz2 'https://downloads.sourceforge.net/project/matroska/mkclean/mkclean-0.8.7.tar.bz2?r=https%3A%2F%2Fwww.matroska.org%2Fdownloads%2Fmkclean.html&ts=1493446534&use_mirror=nchc' && \
  tar -xjf mkclean-0.8.7.tar.bz2 && \
  cd mkclean-0.8.7 && \
  ./configure && \
  make -C mkclean && \
  make install && \
  cd .. && \
  rm -rf mkclean* && \
  wget -O mkvalidator-0.5.0.tar.bz2 'https://downloads.sourceforge.net/project/matroska/mkvalidator/mkvalidator-0.5.0.tar.bz2?r=&ts=1493448048&use_mirror=nchc' && \
  tar -xjf mkvalidator-0.5.0.tar.bz2 && \
  cd mkvalidator-0.5.0 && \
  ./configure && \
  make -C mkvalidator && \
  make install && \
  cd .. && \
  rm -rf mkvalidator* && \
  apt-get purge -y \
          build-essential checkinstall binutils build-essential bzip2 checkinstall \
          cpp cpp-5 dpkg-dev fakeroot g++ g++-5 gcc gcc-5 ifupdown iproute2 \
          isc-dhcp-client isc-dhcp-common libalgorithm-diff-perl libalgorithm-diff-xs-perl \
          libalgorithm-merge-perl libasan2 libatm1 libatomic1 libc-dev-bin libc6-dev libcc1-0 \
          libcilkrts5 libdns-export162 libdpkg-perl libfakeroot libfile-fcntllock-perl \
          libgcc-5-dev libgdbm3 libisc-export160 libisl15 libitm1 liblsan0 libmnl0 libmpc3 \
          libmpfr4 libmpx0 libperl5.22 libquadmath0 libstdc++-5-dev libtsan0 libubsan0 \
          libxtables11 linux-libc-dev make manpages manpages-dev netbase patch perl \
          perl-modules-5.22 rename xz-utils gcc-multilib g++-multilib libxxf86vm-dev \
          libglu1-mesa-dev libxft-dev g++-5-multilib g++-multilib gcc-5-multilib gcc-multilib \
          lib32asan2 lib32atomic1 lib32cilkrts5 lib32gcc-5-dev lib32gcc1 lib32gomp1 lib32itm1 \
          lib32mpx0 lib32quadmath0 lib32stdc++-5-dev lib32stdc++6 lib32ubsan0 libc6-dev-i386 \
          libc6-dev-x32 libc6-x32 libdrm-dev libexpat1-dev libfontconfig1-dev libfreetype6-dev \
          libgl1-mesa-dev libglu1-mesa libglu1-mesa-dev libpng12-dev libpthread-stubs0-dev \
          libx11-dev libx11-doc libx11-xcb-dev libx32asan2 libx32atomic1 libx32cilkrts5 \
          libx32gcc-5-dev libx32gcc1 libx32gomp1 libx32itm1 libx32quadmath0 libx32stdc++-5-dev \
          libx32stdc++6 libx32ubsan0 libxau-dev libxcb-dri2-0-dev libxcb-dri3-dev libxcb-glx0-dev \
          libxcb-present-dev libxcb-randr0 libxcb-randr0-dev libxcb-render0 libxcb-render0-dev \
          libxcb-shape0-dev libxcb-sync-dev libxcb-xfixes0-dev libxcb1-dev libxdamage-dev \
          libxdmcp-dev libxext-dev libxfixes-dev libxft-dev libxft2 libxrender-dev libxrender1 \
          libxshmfence-dev libxxf86vm-dev mesa-common-dev pkg-config x11proto-core-dev \
          x11proto-damage-dev x11proto-dri2-dev x11proto-fixes-dev x11proto-gl-dev \
          x11proto-input-dev x11proto-kb-dev x11proto-render-dev x11proto-xext-dev \
          x11proto-xf86vidmode-dev xorg-sgml-doctools xtrans-dev zlib1g-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY mkvalidator /scripts/mkvalidator
COPY ffmpegvalidator /scripts/ffmpegvalidator
RUN chmod +x /scripts/mkvalidator && \
    chmod +x /scripts/ffmpegvalidator

VOLUME /data
VOLUME /output
CMD ["/scripts/mkvalidator", "/data", "/output"]