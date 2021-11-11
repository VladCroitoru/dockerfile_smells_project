# feesmrt/ubuntu-base-1704
# Docker project for a base ubuntu 17.04 image

FROM ubuntu:17.04

MAINTAINER feesmrt

# Update | Upgrade | Dist-Upgrade | Autoremove
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y dist-upgrade \
    && apt-get -y autoremove

# Install tools
RUN apt-get install -y nano ssh git-core sudo

# Create user: dockeruser | set password: docker | add user to sudoers
RUN useradd -c "Docker standard user" -m -s /bin/bash dockeruser \
    && /bin/bash -c "echo dockeruser:dockeruser | chpasswd" \
    && /bin/bash -c "usermod -a -G sudo dockeruser" \
    && echo "dockeruser ALL=NOPASSWD: ALL" >> /etc/sudoers

# Register user to docker
USER dockeruser
WORKDIR /home/dockeruser
