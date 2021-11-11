FROM ubuntu:latest
MAINTAINER Jon Ferretti

WORKDIR /root

RUN apt-get update
# Base tools
RUN apt-get install -y git vim wget curl tar ssh

# 2.7 and headers
RUN apt-get install -y python python-dev python-distribute python-pip

# Build tools
RUN apt-get install -y build-essential

# Get 3.4
RUN wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tgz

# Altinstall 3.4
RUN tar -xvzf Python-3.4.3.tgz
WORKDIR Python-3.4.3
RUN ./configure --prefix=/usr
RUN make && make altinstall

# Setup dotfiles
WORKDIR /root
RUN git clone https://github.com/LISTERINE/dotfiles.git
RUN mv dotfiles .dotfiles
WORKDIR .dotfiles
RUN /bin/bash -c "source install.sh"

WORKDIR /root
