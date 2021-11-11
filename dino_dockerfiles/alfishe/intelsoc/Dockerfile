FROM library/ubuntu:16.04

MAINTAINER alfishe

# lsb_release doen't work in Docker's Moby
ENV VERSION_CODENAME xenial

# Silense incompatibility between Docker and Ubuntu (eliminates 'debconf: unable to initialize frontend: Dialog' kind of errors)
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Add ARMhf architecture packages support
RUN echo "deb [arch=armhf] http://ports.ubuntu.com/ubuntu-ports ${VERSION_CODENAME} main universe" >> /etc/apt/sources.list

# Be ready for package installation
RUN apt-get --quiet --yes update

# Restore sudo missing in latest docker images release by Canonical
RUN apt-get --quiet --yes install sudo:amd64 && rm -rf /var/lib/apt/lists/*

# Get lists one more time (since /var/lib/apt/lists was wiped out)
RUN apt-get --quiet --yes update


# Install host development packages
RUN apt-get --quiet --yes install \
    make:amd64 \
    u-boot-tools:amd64 \
    libncurses-dev:amd64

# Install ARM cross-platform toolchain
RUN apt-get --quiet --yes install \
    gcc-arm-linux-gnueabihf:amd64 g++-arm-linux-gnueabihf:amd64\
    libc6-armhf-cross:amd64 libc6-dev-armhf-cross:amd64

# Clean up the image
RUN	apt-get clean && \
	apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*


ENV CROSS_COMPILE arm-linux-gnueabihf-

RUN mkdir /work

# Set the working directory to /work (shared folder to be mounted during the run)
WORKDIR /work