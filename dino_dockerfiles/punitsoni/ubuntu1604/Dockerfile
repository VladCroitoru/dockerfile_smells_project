#
# image for ubuntu desktop interactive
#
FROM ubuntu:16.04
MAINTAINER "Punit Soni <punitxsmart@gmail.com>"

# install basic packages
RUN apt-get update && \
    apt-get install -y sudo vim git tmux

# set locale
ENV LANG C.UTF-8

# add user
RUN useradd --create-home --shell /bin/bash punits && \
    echo "punits:change_this" | chpasswd && \
    adduser punits sudo

USER punits
WORKDIR /home/punits

# setup dotfiles
RUN git clone https://github.com/punitsoni/dotfiles.git ~/.dotfiles && \
    ~/.dotfiles/setup.sh -f

# git config
RUN git config --global user.name "Punit Soni" && \
    git config --global user.email "punitxsmart@gmail.com"