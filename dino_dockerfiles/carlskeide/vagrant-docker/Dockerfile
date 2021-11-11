FROM phusion/baseimage:latest

MAINTAINER Carl Skeide "carl@skeide.se"

# System
ENV VAGRANT_USER "vagrant"
ENV VAGRANT_PASS "vagrant"
ENV DEBIAN_FRONTEND noninteractive

# Packages
RUN apt-get -qq update &&\
    apt-get -qq install -y --no-install-recommends \
        make gcc git-core ssh-client rsync \
        screen tmux nano vim curl wget bash-completion &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# User
ADD skel /etc/skel
RUN useradd \
        -md "/home/vagrant" \
        -G docker_env,sudo \
        -s /bin/bash \
        ${VAGRANT_USER} &&\
    echo "${VAGRANT_USER}:${VAGRANT_PASS}" | chpasswd

# SSH
RUN echo "linux" > /etc/container_environment/TERM &&\
    rm -f /etc/service/sshd/down &&\
    /etc/my_init.d/00_regen_ssh_host_keys.sh

# Convenience
VOLUME /vagrant
WORKDIR /vagrant
