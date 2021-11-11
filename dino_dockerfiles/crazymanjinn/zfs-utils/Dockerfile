FROM debian:latest

ENV zol_package="zfsonlinux_6_all.deb" \
  zol_link="http://archive.zfsonlinux.org/debian/pool/main/z/zfsonlinux/"

RUN apt-get update && apt-get install -y \
  curl \
  lsb-release && \
  curl -OL ${zol_link}${zol_package} && dpkg -i ${zol_package} && \
  apt-get -y update && apt-get -y install debian-zfs && \
  rm -rf /var/lib/apt/lists/* && rm ${zol_package}

ENTRYPOINT []
