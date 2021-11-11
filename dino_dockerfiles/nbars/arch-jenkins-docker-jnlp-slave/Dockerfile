FROM nfnty/arch-mini:latest
MAINTAINER Nils Bars <arch@nbars.de>

COPY pacman.conf /etc/pacman.conf

RUN  chmod 644 /etc/pacman.conf && chown root:root /etc/pacman.conf

#Update system and install some packages
RUN pacman -Syyu --noconfirm \
 && pacman -S --noconfirm --needed base-devel git wget nano sudo \
    openssh ccache iputils iproute2 jshon xdelta3 tree jdk8-openjdk

#Replace gcc with gcc-multilib
RUN echo -e "y\ny\ny" | sudo pacman -S gcc-multilib

RUN pacman-key --init && pacman-key --populate archlinux \
 && rm -rf /var/cache/pacman/pkg/*

RUN useradd -m -d /home/jenkins -s /bin/bash jenkins \
    && echo "jenkins:jenkins" | chpasswd \
    && groupadd sudo && gpasswd -a jenkins sudo

#Enable sudo group
RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

#install cower and pacaur
RUN  \
  sudo -u jenkins gpg --keyserver 'hkp://pgp.mit.edu'  --recv-keys 1EB2638FF56C0C53 ; \
  cd /tmp ; \
  sudo -u jenkins wget https://aur.archlinux.org/cgit/aur.git/snapshot/cower.tar.gz ; \
  sudo -u jenkins tar -xzf cower.tar.gz ; \
  cd ./cower ; \
  sudo -u jenkins makepkg -si --noconfirm --needed ; \
  cd .. ; \
  sudo -u jenkins wget https://aur.archlinux.org/cgit/aur.git/snapshot/pacaur.tar.gz ; \
  sudo -u jenkins tar -xzf pacaur.tar.gz ; \
  cd ./pacaur ; \
  sudo -u jenkins makepkg -si --noconfirm --needed

# Default command
CMD ["echo", "No default cmd set!"]
