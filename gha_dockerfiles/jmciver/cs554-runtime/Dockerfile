FROM riscv64/ubuntu:20.04

ENV TZ=US/Mountain
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime

RUN apt update && \
  apt upgrade -y && \
  apt install -y \
    gcc \
    less \
    make \
    python-is-python3 \
    tmux \
    vim-tiny \
    emacs-nox && \  
  apt clean

WORKDIR /root
