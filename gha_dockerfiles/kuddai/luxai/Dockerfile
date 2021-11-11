# This docker file basically replicates the competition environment but using the lux-ai-2021 tool instead

#FROM ubuntu:18.04
# Taken from
# https://hub.docker.com/layers/nvidia/cuda/11.1.1-devel-ubuntu18.04/images/sha256-6e58c8d7dc5b25c095e7fb8c6233d91f4b05a077d13c35ef49328e7478f490c9?context=explore
# IMPORTANT find docker image which matches your cuda driver (see nvidia-smi).
# Otherwise your container may end up with different libcuda.so.* version
# which would conflict with each other.
FROM nvidia/cuda:11.1.1-devel-ubuntu18.04

ARG USER=root
ARG UID=1000
ARG GID=1000

# nvm environment variables
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 14.16.0

# basic setups
RUN apt-get update && apt-get install -y -q --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        unzip \
        sudo \
        curl \
        wget \
        libcudnn8 \
        software-properties-common

RUN groupadd -g $GID -o $USER
RUN useradd -m -u $UID -g $GID -G sudo -o -s /bin/bash $USER
# having sudo just in case
# https://stackoverflow.com/a/58151889
RUN \
    sed -i /etc/sudoers -re 's/^%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^root.*/root ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^#includedir.*/## **Removed the include directive** ##"/g' && \
    echo "$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    echo "Customized the sudoers file for passwordless access to the $USER user!" && \
    echo "$USER user:";  su - $USER -c id

# install nvm
# https://github.com/creationix/nvm#install-script
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash

# install node and npm
RUN . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# confirm installation
RUN node -v
RUN npm -v

# install lux ai

RUN npm install -g @lux-ai/2021-challenge@latest
# RUN chown -R $USER:$USER /usr/local/lib/node_modules/@lux-ai/

# install tooling for other languages

# Java
RUN apt-get install -y default-jre

# Python
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
# set python3.8 as default
# RUN ln -s python3.8 /usr/bin/python


# C++
RUN apt-get install g++ -y

# OUR CODE
RUN npm install -g serve @lux-ai/2021-challenge@latest
RUN apt update && \
    apt install -y python3-dev \
    pkg-config libhdf5-dev \
    vim

RUN pip3 install -U pip

WORKDIR /lux_ai
COPY requirements.txt /lux_ai
RUN ls /lux_ai
RUN pip3 install -r /lux_ai/requirements.txt
RUN chown -R $USER:$USER /usr/local/

# Monkey patch lux_ai runner
RUN mkdir -p /lux_ai/infra
COPY infra/monkey_patch_luxai.py /lux_ai/infra/monkey_patch_luxai.py
RUN python3 /lux_ai/infra/monkey_patch_luxai.py
