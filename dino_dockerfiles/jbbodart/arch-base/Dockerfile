FROM base/archlinux:2017.10.01
MAINTAINER jbbodart

# update packages
#################

RUN curl -o /etc/pacman.d/mirrorlist "https://www.archlinux.org/mirrorlist/?country=all&protocol=https&ip_version=4&use_mirror_status=on" && \
  sed -i 's/^#//' /etc/pacman.d/mirrorlist

#RUN dirmngr </dev/null && \
#  pacman-key --populate && \
#  pacman-key --refresh-keys && \
RUN  pacman -Sy --noprogressbar --noconfirm && \
  pacman -S --force openssl --noconfirm && \
  pacman -S pacman --noprogressbar --noconfirm && \
  pacman-db-upgrade && \
  pacman -Syyu --ignore filesystem --noprogressbar --noconfirm

# additional files
##################

# add install bash script
ADD install.sh /root/install.sh

# install app
#############

# run bash script to set locale, install supervisor and cleanup
RUN chmod +x /root/install.sh && \
	/bin/bash /root/install.sh

# env
#####

# set environment variables for user nobody
ENV HOME /home/nobody

# set environment variable for terminal
ENV TERM xterm

# set environment variables for language
ENV LANG en_US.UTF-8

# additional files
##################

# add supervisor configuration file
ADD supervisord.conf /etc/supervisord.conf
