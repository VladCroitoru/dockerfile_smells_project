# DOCKER-VERSION 1.2.0

FROM base/archlinux:latest
MAINTAINER "Matthias Adler" <macedigital@gmail.com>

# remove unneeded pkgs, update and clean cache
RUN pacman -Rss --noconfirm cronie device-mapper dhcpcd diffutils file \
gettext nano inetutils netctl iproute2 iputils vi psmisc \
sysfsutils texinfo usbutils which; \
pacman -Syu --force --noconfirm; \
pacman -Scc --noconfirm

# remove man pages and locale data
RUN rm -rf /archlinux/usr/share/locale && rm -rf /archlinux/usr/share/man

# clean unneeded services
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /lib/systemd/system/graphical.target.wants/*; \
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

# switch default target from graphical to multi-user
RUN systemctl set-default multi-user.target 

# systemd inside a container
ENV container docker
VOLUME [ "/sys/fs/cgroup" ]

CMD ["/usr/sbin/init"]
