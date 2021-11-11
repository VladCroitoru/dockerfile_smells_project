#
# based on haron/vim Dockerfile
#
FROM ubuntu:14.04

MAINTAINER Lucas Benedicic <benedicic@cscs.ch>

# environment variables
ENV DEBIAN_FRONTEND noninteractive

# install software
RUN apt-get update                          && \
    apt-get install -y build-essential   \
                       cmake             \
                       git               \
                       python-dev        \
                       silversearcher-ag \
                       vim               \
                       wget                 && \
    rm -rf /var/lib/apt/lists

# user and locale configuration
RUN useradd dev                                                     && \
    cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime             && \
    dpkg-reconfigure locales                                        && \
    locale-gen en_US.UTF-8                                          && \
    /usr/sbin/update-locale LANG=en_US.UTF-8

WORKDIR /home/dev
ENV HOME /home/dev
ENV LC_ALL en_US.UTF-8 
RUN chown --recursive dev:dev $HOME
USER dev
RUN mkdir -p $HOME/src

# setup pathogen vim plugin manager
RUN mkdir -p $HOME/.vim/autoload $HOME/.vim/bundle          && \
    wget -P $HOME/.vim/autoload https://tpo.pe/pathogen.vim && \
    echo "execute pathogen#infect()" >> $HOME/.vimrc        && \
    echo "syntax on"                 >> $HOME/.vimrc        && \
    echo "filetype plugin indent on" >> $HOME/.vimrc

# include the user's vimrc
ADD vimrc .vimrc

#
# -- Vim plugins --
#

# Sensible 
RUN git clone https://github.com/tpope/vim-sensible.git $HOME/.vim/bundle/vim-sensible      && \
# Airline
    git clone https://github.com/bling/vim-airline.git $HOME/.vim/bundle/vim-airline        && \
# CtrlP
    git clone https://github.com/kien/ctrlp.vim.git $HOME/.vim/bundle/ctrlp.vim             && \
# Git
    git clone https://github.com/tpope/vim-fugitive.git $HOME/.vim/bundle/vim-fugitive      && \
# Git in the gutter
    git clone https://github.com/airblade/vim-gitgutter.git $HOME/.vim/bundle/vim-gitgutter && \
# Silver search
    git clone https://github.com/rking/ag.vim.git $HOME/.vim/bundle/ag.vim                  && \
# YouCompleteMe
    git clone https://github.com/Valloric/YouCompleteMe.git $HOME/.vim/bundle/YouCompleteMe && \
    cd $HOME/.vim/bundle/YouCompleteMe                                                      && \
    git submodule update --init --recursive                                                 && \
    ./install.sh --clang-completer

USER root
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["vim"]
