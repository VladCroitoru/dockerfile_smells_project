FROM ubuntu:bionic

MAINTAINER Mush Mo <mush@pandorica.io>

ENV DEBIAN_FRONTEND noninteractive

# setting up ssh
RUN mkdir -p /var/run/sshd
RUN useradd dev -m -p password -s /bin/bash
RUN echo "dev:password" | chpasswd
RUN passwd -e dev

ADD ./deltmp /usr/bin/deltmp
RUN chmod ugo+x /usr/bin/deltmp

# update
RUN apt-get update && \
    apt-get install -y \
    software-properties-common \
    sudo \
    curl \
    locales

# chinese language package
RUN locale-gen zh_CN.UTF-8

ADD extra.list /etc/apt/sources.list.d/extra.list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4

RUN apt-get update && \
    apt-get install -y  --allow-unauthenticated \
    build-essential \
    clang \
    cmake \
    coffeescript \
    git \
    git-all \
    libclang-dev \
    libfreetype6-dev \
    libjpeg8-dev \
    libpcre3-dev \
    libssl-dev \
    lsof \
    mercurial \
    mlocate \
    libmemcached-dev \
    zlib1g-dev \
    mongodb-org-shell \
    mongodb-org-tools \
    openssh-client \
    openssh-server \
    python3.6 \
    python3.6-dev \
    python3-pip \
    rpl \
    silversearcher-ag \
    swig \
    tmux \
    tree \
    vim \
    xtail \
    ack-grep \
    wget \
    redis-tools \
    libxml2 \
    libxslt-dev \
    libxml2-dev \
&& rm -rf /var/lib/apt/lists/*

RUN echo "dev ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# install vim-plugin
COPY ./vimrc /etc/vim/vimrc.local 
RUN git clone https://github.com/gmarik/Vundle.vim.git /usr/share/vim/vimfiles/bundle/Vundle.vim
RUN vim -c 'PluginInstall' -c 'qa!'
ENV YCM_DIR /usr/share/vim/vimfiles/bundle/YouCompleteMe
WORKDIR $YCM_DIR
RUN git submodule update --init --recursive
RUN python3 ./install.py --clang-completer

RUN mkdir /home/dev/workspace

COPY bashrc /home/dev/.bashrc

RUN pip3 install virtualenv flake8
RUN chown -R dev:dev /home/dev

ENTRYPOINT ["/usr/sbin/sshd", "-f", "/etc/ssh/sshd_config", "-D"]
