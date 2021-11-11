FROM ubuntu:14.04

RUN apt-get update && \
  apt-get install -y --reinstall build-essential libncurses-dev rsync unzip bc git python wget && \
  git clone https://github.com/buildroot/buildroot.git /buildroot && \
  git clone https://github.com/Croncron85/buildroot-openvpn-tarmaker.git /tarmaker && \
  chmod +x /tarmaker/docker/openvpn/post.sh && \
  rsync -av /tarmaker/ /buildroot/ && \
  rm -rf /tarmaker && \
  cd /buildroot && \
  make x86_64_openvpn_defconfig && \
  make clean all && \
  mkdir -p /output/images && \
  mv /buildroot/output/images/rootfs.tar /output/images/rootfs.tar  && \
  apt-get purge -y --auto-remove build-essential libncurses-dev rsync unzip bc git python wget && \
  cd / && \
  rm -rf /buildroot
