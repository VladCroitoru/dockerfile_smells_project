## -*- docker-image-name: "opamp/archlinux" -*-
FROM nfnty/arch-mini:latest
MAINTAINER opamp_sando <opampg@gmail.com>

RUN pacman -Syu --noconfirm binutils which file fakeroot grep make gawk util-linux sed patch git sudo > /dev/null &&rm -f /etc/sudoers
ADD sudoers /etc/sudoers
RUN chown root:root /etc/sudoers && chmod 440 /etc/sudoers
RUN useradd -m -d /home/user -s /bin/bash -g users -G users,wheel user

# Install yaourt
ADD pacman.conf.patch /tmp/pacman.conf.patch
RUN patch /etc/pacman.conf < /tmp/pacman.conf.patch && rm -f /tmp/pacman.conf.patch
RUN pacman -Syu yaourt --noconfirm > /dev/null

ONBUILD RUN pacman -Syu --noconfirm > /dev/null
