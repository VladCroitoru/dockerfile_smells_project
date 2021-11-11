# Start from an Ubuntu 16.04 image
FROM ubuntu:16.04

MAINTAINER Nicolas Bigaouette <nbigaouette@rogue-research.com>

# Update apt-get's database
RUN apt-get --quiet --yes update

# Install Yocto's dependencies
RUN apt-get --quiet --yes install \
    gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm

# Install our dependencies
RUN apt-get --quiet --yes install \
    sudo cpio cvs subversion tree libxt-dev bmap-tools openssh-client

# Clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create a 'dockeruser' user and group, add it to sudoers and switch to it
RUN /usr/sbin/groupadd --gid 1000 dockeruser && \
    /usr/sbin/useradd --create-home --shell /bin/bash dockeruser --uid 1000 --gid 1000 && \
    echo "dockeruser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Create a Yocto build directory
RUN mkdir -p /yocto/build && chown 1000:1000 /yocto/build

# Switch to our dockeruser user
USER dockeruser
