# Basic Arch Linux based OpenWrt buildroot image
FROM base/archlinux

MAINTAINER Jannis Pinter <jannis@pinterjann.is>

RUN pacman -Sy --noconfirm archlinux-keyring &&\ 
pacman -Su --noconfirm --needed subversion asciidoc bash bc binutils fastjar \
	flex git gcc util-linux intltool make cdrkit openssl patch \
	perl-extutils-makemaker rsync sdcc unzip wget gettext libxslt \
	boost bin86 sharutils b43-fwcutter sudo libunistring &&\
useradd -m openwrt &&\
echo 'openwrt ALL=NOPASSWD: ALL' > /etc/sudoers.d/openwrt &&\
sudo -iu openwrt git clone git://git.openwrt.org/openwrt.git &&\
sudo -iu openwrt openwrt/scripts/feeds update

USER openwrt
WORKDIR /home/openwrt/openwrt/
CMD ["/bin/bash"] 
