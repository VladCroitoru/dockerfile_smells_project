# -*- sh -*-
FROM base/archlinux
MAINTAINER mjhooker, mjhooker@gmail.com

RUN echo -e "[multilib]\nInclude = /etc/pacman.d/mirrorlist" > /tmp/multilib
RUN cat /etc/pacman.conf /tmp/multilib > /tmp/pacman.conf
RUN mv /tmp/pacman.conf /etc/pacman.conf
RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm curl unzip lib32-zlib lib32-ncurses lib32-bzip2
WORKDIR /home

RUN curl get.pharo.org/stable+vm | bash
RUN echo "Pharo installed"
