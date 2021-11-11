FROM ubuntu:latest
MAINTAINER lysu <sulifx@gmail.com>

RUN apt-get update &&  apt-get install  -y \
    man \
    build-essential \
    cmake \
    curl \
    git \
    libboost-dev \
    libboost-filesystem-dev \
    libboost-program-options-dev \
    libboost-regex-dev \
    libboost-system-dev \
    libboost-thread-dev \
    libopenmpi-dev \
    openmpi-bin \
    openmpi-common  \
    openssh-client \
    clang-3.7 \
    clang-format \
    libomp-dev \
    vim \
    emacs \
    netcat \
    unzip \
    valgrind \
    net-tools \
    doxygen \
    tmux \
    cscope \
    global \
    gdb \
    zsh \
    xfonts-utils  \
    locales \
    ctags \
    xdg-utils \
    python-dev \
    python-pip \
    python-setuptools \
    rubygems \
    curl \
    fontconfig \
    ca-certificates \
    pkg-config \
    autoconf \
    libxml2-dev \
    libglib2.0-dev \
    libgsl0-dev \
    libcurl4-gnutls-dev \
    ack-grep \
    psmisc \
    tcpdump \
    iputils-ping \
 && apt-get clean

RUN cd /tmp \
 && curl https://www.samba.org/ftp/ccache/ccache-3.2.5.tar.xz | tar xJ \
 && cd ccache-3.2.5 \
 && ./configure \
 && make \
 && make install \
 && cd \
 && rm -r /tmp/ccache-3.2.5

ENV CCACHE_DIR=/ccache

RUN update-alternatives --install /usr/bin/clang   clang   /usr/bin/clang-3.7 999 \
 && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.7 999 \
 && update-alternatives --install /usr/bin/cc  cc  /usr/bin/clang-3.7 999 \
 && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-3.7 999

ENV CC="ccache clang" CXX="ccache clang++"

RUN git clone git://github.com/amix/vimrc.git ~/.vim_runtime \
    && sh ~/.vim_runtime/install_awesome_vimrc.sh

RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
    && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
    && chsh -s /bin/zsh

RUN git clone https://github.com/Valloric/YouCompleteMe ~/.vim_runtime/sources_non_forked/YouCompleteMe

RUN cd ~/.vim_runtime/sources_non_forked/YouCompleteMe && git submodule update --init --recursive && ./install.sh --clang-completer

RUN git clone https://github.com/vim-scripts/gtags.vim.git ~/.vim_runtime/sources_non_forked/gtags.vim

RUN git clone https://github.com/rhysd/vim-clang-format.git ~/.vim_runtime/sources_non_forked/vim-clang-format

ADD my_configs.vim /root/.vim_runtime/my_configs.vim
ADD ycm_extra_conf.py /root/.ycm_extra_conf.py
ADD tmux.conf /root/.tmux.conf
ENV TERM=xterm-256color

ADD sources.list /etc/apt/sources.list
RUN apt-get update
