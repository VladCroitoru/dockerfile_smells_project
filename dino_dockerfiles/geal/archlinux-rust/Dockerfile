# -*- sh -*-
FROM base/archlinux
MAINTAINER Geoffroy Couprie, contact@geoffroycouprie.com

RUN echo -e "[multilib]\nInclude = /etc/pacman.d/mirrorlist" > /tmp/multilib
RUN cat /etc/pacman.conf /tmp/multilib > /tmp/pacman.conf
RUN mv /tmp/pacman.conf /etc/pacman.conf
RUN pacman-key --refresh-keys
RUN pacman -Syu --noconfirm
RUN pacman-db-upgrade
RUN pacman -S --noconfirm unzip lib32-zlib binutils llvm gcc
RUN pacman -S --noconfirm curl lib32-ncurses lib32-bzip2 lib32-libstdc++5 lib32-openssl

RUN curl -sSf https://static.rust-lang.org/rustup.sh | sh -s -- --channel=nightly --disable-sudo -y

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
