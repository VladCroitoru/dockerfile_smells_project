FROM scratch

MAINTAINER apporc <apporc@gmail.com>

ADD bootstraps/arch-mini-bootstrap.tar.xz /

RUN echo 'Server = http://mirrors.kernel.org/archlinux/$repo/os/$arch' >> /etc/pacman.d/mirrorlist
RUN pacman-key --init && pacman-key --populate archlinux 

CMD ["/bin/bash"]
