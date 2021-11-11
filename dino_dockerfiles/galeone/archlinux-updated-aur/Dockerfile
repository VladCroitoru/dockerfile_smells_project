FROM base/archlinux
MAINTAINER Paolo Galeone <nessuno@nerdz.eu>

RUN pacman -Syy pacman haveged archlinux-keyring --noconfirm && haveged -w 1024 -v 1 && \
    pacman-key --init && pacman-key --populate archlinux && pacman-db-upgrade && pacman -Syy

RUN pacman -Su base-devel yajl wget ca-certificates ca-certificates-cacert \
    openssl ca-certificates-mozilla ca-certificates-utils git subversion \ 
    nodejs npm gcc-libs --noconfirm

RUN useradd -m -s /bin/bash aur && echo "aur ALL = NOPASSWD: /usr/bin/pacman" >> /etc/sudoers
RUN mkdir -p /etc/pki/tls/certs && \
    ln -s /etc/ca-certificates/extracted/tls-ca-bundle.pem /etc/pki/tls/certs/ca-bundle.crt

USER aur
ENV PATH /usr/bin/core_perl:$PATH

RUN cd /tmp && curl -O https://aur.archlinux.org/cgit/aur.git/snapshot/cower-git.tar.gz && \
    tar zxvf cower-git.tar.gz && cd cower-git && makepkg

RUN cd /tmp && curl -O https://aur.archlinux.org/cgit/aur.git/snapshot/expac-git.tar.gz && \
    tar zxvf expac-git.tar.gz && cd expac-git && makepkg

USER root
RUN pacman -U /tmp/cower-git/*.xz /tmp/expac-git/*.xz --noconfirm

USER aur
RUN cd /tmp && curl -O https://aur.archlinux.org/cgit/aur.git/snapshot/pacaur.tar.gz && \
    tar zxvf pacaur.tar.gz && cd pacaur && makepkg

RUN sudo pacman -U /tmp/pacaur/*.xz --noconfirm && rm -rf /tmp/*
