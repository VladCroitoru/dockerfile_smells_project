FROM ubuntu:trusty
MAINTAINER YI-HUNG JEN <yihungjen@gmail.com>

# install core components
RUN apt-get update && apt-get install -y \
    curl \
    dnsutils \
    git \
    htop \
    jq \
    tmux \
    telnet \
    vim \
    vim-gtk \
    wget \
    xclip \
    xsel \
    zip

# setup local info
RUN locale-gen en_US.UTF-8

# the user that will run this container
RUN useradd -s /bin/bash -d /home/yihungjen -G sudo -m yihungjen
RUN echo "yihungjen:!@mYihungJ3n" | chpasswd

COPY entrypoint.sh /entrypoint.sh
COPY profile ./.profile

# get instance of workspaceenv for workspace configuration
COPY . /home/yihungjen/.workspaceenv
ENV HOME /home/yihungjen
WORKDIR /home/yihungjen/.workspaceenv

# build essentials
RUN ./install-build-essential

# install golang
RUN ./install-golang

# install nodejs and tools written with nodejs
RUN ./install-nodejs

# install python and tools written with python
RUN ./install-python

# install docker toolchain
RUN ./install-docker-toolchain

# setup group and permission for docker sock
RUN groupadd -g 999 docker
RUN usermod -aG docker yihungjen

# install misc stuff
RUN ./install-misc

# setup workspace with bootsrap command
RUN ./bootstrap

# VOLUME hooks for security settings
VOLUME /home/yihungjen/.aws
VOLUME /home/yihungjen/.gnupg
VOLUME /home/yihungjen/.ssh

# make sure permission is correct
WORKDIR /home/yihungjen
RUN chown -R yihungjen:yihungjen ./

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash", "-l"]
