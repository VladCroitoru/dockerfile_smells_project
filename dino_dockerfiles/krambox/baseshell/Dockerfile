FROM ubuntu:16.04

# Locales
ENV LANGUAGE=en_US.UTF-8
ENV LANG=en_US.UTF-8
COPY xterm-256color-italic.terminfo /root

RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8

# Common packages
RUN apt-get update && apt-get install -y \
      locales \
      build-essential \
      curl \
      git  \
      iputils-ping \
      jq \
      libncurses5-dev \
      libevent-dev \
      net-tools \
      netcat-openbsd \
      rubygems \
      ruby-dev \
      silversearcher-ag \
      socat \
      software-properties-common \
      tmux \
      tzdata \
      wget \
      zsh && \
      locale-gen en_US.UTF-8 && \
      tic /root/xterm-256color-italic.terminfo && \
      wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

# Colors and italics for tmux
ENV TERM=xterm-256color-italic


VOLUME ["/work"]
WORKDIR /work

RUN chsh -s /usr/bin/zsh
