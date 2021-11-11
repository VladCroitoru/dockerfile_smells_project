FROM ubuntu:focal

LABEL maintainer="Mark He Huang <mark.h.huang@gmail.com>"

USER root 

ENV DEBIAN_FRONTEND=noninteractive

ENV TZ=Asia/Singapore

# RUN apt-get update && apt-get install apt-file -y && apt-file update

ENV TERM=xterm-256color

RUN APT_INSTALL="apt-get install -y --no-install-recommends" && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
    apt-utils \ 
    ca-certificates \
    sudo \
    wget \
    curl 

# Set Timezone data
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

# variable HOME may not be set, set to /root anyway
WORKDIR ${HOME:-/root}

# Copy dotfiles
COPY . ./dotfiles

# Install dotfiles
RUN cd dotfiles && ./install 

# Initialize zsh
CMD cd ${HOME:-/root} && zsh