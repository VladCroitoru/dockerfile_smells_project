FROM pritunl/archlinux:2016-10-08
MAINTAINER vonpupp <vonpupp@gmail.com>

#RUN pacman -S --needed --noconfirm reflector; reflector --verbose -l 5 -p http --sort rate --save /etc/pacman.d/mirrorlist; pacman -Rs --noconfirm reflector
RUN pacman -S --needed --noconfirm ansible python2 python python2-pip sudo base-devel git systemd

