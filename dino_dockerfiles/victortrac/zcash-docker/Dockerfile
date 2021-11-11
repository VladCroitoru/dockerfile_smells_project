FROM ubuntu:latest
MAINTAINER Victor Trac <victor.trac@gmail.com>

ENV VERSION v1.0.0
ENV BUILD_PACKAGES build-essential pkg-config libc6-dev m4 g++-multilib autoconf libtool ncurses-dev unzip git python zlib1g-dev wget bsdmainutils automake

# Install, copy binaries to /usr/local/bin, cleanup
RUN apt-get update \
  && apt-get install -y ${BUILD_PACKAGES} \
  && git clone https://github.com/zcash/zcash.git \
  && cd zcash/ \
  && git checkout ${VERSION} \
  && bash /zcash/zcutil/fetch-params.sh \
  && bash /zcash/zcutil/build.sh -j$(nproc) \
  && cp /zcash/src/zcash-* /usr/local/bin \
  && cp /zcash/src/zcashd /usr/local/bin \
  && apt-get remove --purge -y ${BUILD_PACKAGES} `apt-mark showauto` \
  && apt autoremove -y \
  && apt-get install -y libgomp1 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /root/.ccache \
  && rm -rf /zcash 

CMD /usr/local/bin/zcashd
