# archlinux
# VERSION 2.0.0
#
# A fully updated Arch Linux base image
# Based on https://github.com/logankoester/docker-archlinux

FROM base/archlinux
MAINTAINER Maikel Wever <maikelwever@gmail.com>

RUN curl -o /etc/pacman.d/mirrorlist "https://www.archlinux.org/mirrorlist/?country=all&protocol=https&ip_version=6&use_mirror_status=on" && \
  sed -i 's/^#//' /etc/pacman.d/mirrorlist

ONBUILD RUN pacman-key --populate && \
  pacman-key --refresh-keys && \
  pacman -Sy --noprogressbar --noconfirm && \
  pacman -S --force openssl --noconfirm && \
  pacman -S pacman --noprogressbar --noconfirm && \
  pacman-db-upgrade && \
  pacman -Syy --noprogressbar --noconfirm archlinux-keyring && \
  pacman -Su --noprogressbar --noconfirm
