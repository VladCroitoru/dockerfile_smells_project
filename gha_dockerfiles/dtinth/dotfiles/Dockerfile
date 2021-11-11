FROM buildpack-deps:buster AS base

RUN apt-get update && apt-get install -y sudo && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd -rm -d /home/user -s /bin/bash -G sudo -u 1000 user
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER user

WORKDIR /dotfiles
COPY --chown=user:user ./ ./
RUN ./install

FROM base

RUN sudo apt-get update && sudo apt-get install -y tmux neovim htop build-essential
