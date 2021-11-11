FROM debian:jessie-slim

MAINTAINER Tim Schruben <tim.schruben@gmail.com>

# User config
ENV SHELL="/bin/bash" \
    HOME=/home/developer \
    TERM=xterm-256color

RUN adduser --shell $SHELL --disabled-password --quiet developer

RUN apt-get update && \
    apt-get install -y \
                    vim \
                    git \
                    tree \
                    curl \
                    wget \
                    less \
                    ctags \
                    libevent-dev \
                    gcc \
                    ncurses-dev \
                    make \
                    automake \
                    pkg-config && \
    apt-get clean

RUN git clone --depth 1 https://github.com/tmux/tmux.git && \
    cd tmux && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install

ADD dotfiles/ $HOME
ADD vimrc $HOME/.vimrc

RUN mkdir -p $HOME/.tmux/plugins && \
    cd $HOME/.tmux/plugins && \
    git clone --depth 1 --recursive https://github.com/tmux-plugins/tmux-continuum.git && \
    git clone --depth 1 https://github.com/tmux-plugins/tmux-resurrect.git && \
    git clone --depth 1 https://github.com/tmux-plugins/tpm.git

RUN mkdir -p $HOME/.vim/bundle && \
    cd $HOME/.vim/bundle && \
    git clone --depth 1 --recursive https://github.com/scrooloose/nerdtree.git && \
    git clone --depth 1 --recursive https://github.com/vim-syntastic/syntastic.git && \
    git clone --depth 1 --recursive https://github.com/tpope/vim-sensible.git && \
    git clone --depth 1 --recursive https://github.com/sheerun/vim-polyglot.git && \
    git clone --depth 1 --recursive https://github.com/tpope/vim-obsession.git

RUN apt-get install sudo && apt-get clean
RUN echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers
RUN adduser developer sudo && adduser developer adm

ENV LC_ALL C.UTF-8
ENV LANG $LC_ALL
ENV LANGUAGE $LC_ALL  
#RUN dpkg-reconfigure locales

USER developer

