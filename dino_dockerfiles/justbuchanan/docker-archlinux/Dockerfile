FROM archlinux/base
MAINTAINER Justin Buchanan <justbuchanan@gmail.com>

# update/init keyring
RUN pacman-key --init
RUN pacman-key --populate archlinux

# update keyring
RUN pacman --noconfirm -Sy archlinux-keyring

# update packages and clear cache
RUN pacman -Syyu --noconfirm && pacman -Scc --noconfirm

# upgrade db
RUN pacman-db-upgrade
