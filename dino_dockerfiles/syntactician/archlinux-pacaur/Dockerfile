FROM greyltc/archlinux:latest
MAINTAINER Edward Hernandez

RUN pacman -q --noconfirm -Syyuu
RUN pacman -q --noconfirm -S  \
		base-devel    \
		curl          \
		expac         \
		git           \
		openssl       \
		yajl

RUN sed -i '/NOPASSWD/s/\#//' /etc/sudoers
RUN useradd -r -g wheel build

WORKDIR /build
RUN chown -R build /build

WORKDIR /home/build
RUN chown -R build /home/build
USER build
RUN gpg --recv-keys --keyserver hkp://pgp.mit.edu 1EB2638FF56C0C53

WORKDIR /build
RUN git clone https://aur.archlinux.org/cower.git
WORKDIR /build/cower
RUN makepkg --noconfirm -i

WORKDIR /build
RUN git clone https://aur.archlinux.org/pacaur.git
WORKDIR /build/pacaur
RUN makepkg --noconfirm -i

USER root

RUN sed -i '/silent/s/true/false/; /silent/s/#//' /etc/xdg/pacaur/config
ENV AURDEST /build
ENV PACMAN pacaur

WORKDIR /
RUN paccache -r -k0
RUN pacaur -Scc
RUN rm -rf /usr/share/man/*
RUN rm -rf /tmp/*
RUN rm -rf /var/tmp/*
