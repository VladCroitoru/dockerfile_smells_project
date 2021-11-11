FROM base/archlinux:latest

ENV MIRROR_SERVER http://mirrors.kernel.org/archlinux/\$repo/os/\$arch
# ENV MIRROR_SERVER http://mirrors.163.com/archlinux/\$repo/os/\$arch
# ENV MIRROR_SERVER http://mirror.rackspace.com/archlinux/\$repo/os/\$arch

RUN echo "[options]" >> /etc/pacman.conf \
  && echo "SigLevel = Never" >> /etc/pacman.conf \
  && echo "Server = $MIRROR_SERVER" > /etc/pacman.d/mirrorlist

RUN pacman-key --init \
  && pacman-key --refresh-keys || : \
  && pacman-key --populate archlinux || : \
  && pacman -Syyu --noconfirm \
  && pacman-db-upgrade

RUN pacman -S clearsilver --noconfirm

WORKDIR /root
CMD ["/bin/bash"]
