FROM ubuntu:14.04

MAINTAINER Adi Baron <adi.baron@takadu.com>

# apt stuff
RUN \
  apt-get update && \
  apt-get install ca-certificates curl wget git zsh -y

# user
RUN \
  useradd -s /usr/bin/zsh -m -p "$1$zyG3jH9L$jkVJbHvm5DUnXDARmZOqY1" takadu && \
  usermod -a -G sudo takadu

# switch to takadu user
USER takadu
WORKDIR /home/takadu

# oh-my-zsh
RUN \
  git clone git://github.com/robbyrussell/oh-my-zsh.git .oh-my-zsh && \
  cp .oh-my-zsh/templates/zshrc.zsh-template .zshrc && \
  sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="sonicradish"/' .zshrc && \
  sed -i 's/plugins=(git)/plugins=(z)/' .zshrc

# back to root
USER root
WORKDIR /
