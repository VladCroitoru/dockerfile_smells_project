FROM debian:jessie
LABEL maintainer "mikael.brorsson@gmail.com"

ENV BUILDROOT_VERSION buildroot-2017.02

COPY fa526_musl_defconfig fa526_uclibc_defconfig /opt/

RUN \
  apt-get update && \
  apt-get install -y \
    build-essential \
    wget \
    cpio \
    python \
    unzip \
    rsync \
    bc \
    subversion \
    squashfs-tools \
    libncurses5-dev \
    git && \
  \
  \
  echo "====> clean up..." && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  \
  \
  echo "====> preparing buildroot" && \
  mkdir -p /src && \
  wget -q https://buildroot.uclibc.org/downloads/$BUILDROOT_VERSION.tar.gz -O - | tar xzf - -C /src && \
  mkdir -p /src/$BUILDROOT_VERSION/output && \
  mkdir -p /images && \
  ln -sf /images /src/$BUILDROOT_VERSION/output/images && \
  mv /opt/*_defconfig /src/$BUILDROOT_VERSION/configs/ && \
  \
  \
  echo "====> building for uClibc" && \
  cd /src/$BUILDROOT_VERSION && \
  make fa526_uclibc_defconfig && \
  make toolchain && \
  cd output/host && \
  tar czf toolchain-arm-buildroot-linux-uclibcgnueabi.tar.gz usr/ && \
  mv toolchain-arm-buildroot-linux-uclibcgnueabi.tar.gz /opt/ && \
  cd ../.. && \
  make clean && \
  \
  \
  echo "====> building for Musl" && \
  cd /src/$BUILDROOT_VERSION && \
  make fa526_musl_defconfig && \
  make toolchain && \
  cd output/host && \
  tar czf toolchain-arm-buildroot-linux-musleabi.tar.gz usr/ && \
  mv toolchain-arm-buildroot-linux-musleabi.tar.gz /opt/ && \
  cd ../.. && \
  make clean && \
  \
  rm -rf dl/*

VOLUME ["/images"]
