## -*- docker-image-name: "opamp/archlinux" -*-
FROM archlinux/base
MAINTAINER opamp_sando <opampg@gmail.com>

RUN useradd -m -d /home/user -s /bin/bash -g users -G users,wheel user
RUN pacman -Syu --noconfirm binutils fakeroot make git sudo > /dev/null &&rm -f /etc/sudoers
ADD sudoers /etc/sudoers
RUN chown root:root /etc/sudoers && chmod 440 /etc/sudoers

ONBUILD RUN pacman -Syu --noconfirm > /dev/null
