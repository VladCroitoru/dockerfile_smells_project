FROM base/archlinux:2017.08.01
RUN pacman -Syu --noconfirm && pacman -S --noconfirm git openssh tar gzip ca-certificates base-devel gcc clang cmake sfml python xorg xorg-server xorg-apps xorg-server-xvfb
RUN Xvfb :100 -screen 0 640x480x24  -fbdir /var/tmp&
