FROM wsbu/toolchain-native:v0.1.6

RUN dpkg --add-architecture i386 && apt-get update && apt-get install --yes \
  lib32z1 \
  libc6-i386 \
  libstdc++6:i386 \
  && rm --recursive --force /var/lib/apt/lists/* \
  && git clone --depth=1 --progress --verbose --branch binaries \
  https://github.com/wsbu/toolchain-arm9.git /binaries \
  && yes | /binaries/eldk/install -d /opt/eldk/4.2 arm \
  && ln -sf 4.2/arm /opt/eldk/arm \
  && cp -r /binaries/eldk-5.6 /opt \
  && rm -rf /binaries

ENV WSBU_C_COMPILER /opt/eldk/4.2/usr/bin/arm-linux-gnueabi-gcc
ENV WSBU_CXX_COMPILER /opt/eldk/4.2/usr/bin/arm-linux-gnueabi-g++
ENV WSBU_C11_COMPILER /opt/eldk-5.6/armv5te/sysroots/i686-eldk-linux/usr/bin/arm-linux-gnueabi/arm-linux-gnueabi-g++
ENV WSBU_C11_FLAGS \
  -isystem /opt/eldk-5.6/armv5te/sysroots/armv5te-linux-gnueabi/usr/include \
  -isystem /opt/eldk-5.6/armv5te/sysroots/armv5te-linux-gnueabi/usr/include/c++ \
  -isystem /opt/eldk-5.6/armv5te/sysroots/armv5te-linux-gnueabi/usr/include/c++/arm-linux-gnueabi
