# Use when bootstrapping
#FROM rpheuts/arch-build 

FROM rpheuts/archlinux

RUN mkdir /run/shm
RUN mkdir /work

COPY mkimage-arch.sh /work/mkimage-arch.sh
COPY mkimage-arch-pacman.conf /work/mkimage-arch-pacman.conf

RUN pacman -S --noconfirm archiso
RUN pacman -S --noconfirm expect

WORKDIR /work/
ENTRYPOINT exec /work/mkimage-arch.sh
