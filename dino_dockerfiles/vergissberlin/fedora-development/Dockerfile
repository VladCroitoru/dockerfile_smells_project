FROM fedora

WORKDIR /root

RUN dnf -yq update &&\
    dnf install -yq \
      bats \
      curl \
      figlet \
      findutils \
      git \
      make \
      mc \
      powerline \
      powerline-fonts \
      tmux \
      tmux-powerline \
      siege \
      wget \
      vim \
      vim-powerline

RUN pip install powerline-gitstatus

COPY setup /
