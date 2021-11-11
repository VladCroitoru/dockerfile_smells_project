FROM ubuntu:18.04

MAINTAINER Lei YU mine260309@gmail.com

# Replace sources.list with mirror in China
# COPY apt-source-cn-16.04.list /etc/apt/sources.list

# Update package repository
RUN apt-get update

# Install g++, git, zlib, etc
RUN apt-get install -y build-essential g++ zlib1g-dev libbz2-dev
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get install -y bash-completion dos2unix ftp gcc-multilib \
                       gdb ghex gitk libboost-all-dev libc6-dbg meld python \
                       quilt wget zip ctags
RUN apt-get install -y git vim tmux curl
RUN apt-get install -y locales
RUN apt-get install -y chrpath cpio gawk texinfo

# For arm64 uefi build
RUN apt-get install -y acpica-tools gcc-aarch64-linux-gnu python3-distutils uuid-dev

# Add user `mine`, change to your favorite name
RUN useradd -ms /bin/bash mine && echo "mine:mine" | chpasswd && adduser mine sudo
RUN mkdir -p /home/mine && chown -R mine:mine /home/mine
USER mine
WORKDIR /home/mine
RUN git clone git://github.com/andsens/homeshick.git /home/mine/.homesick/repos/homeshick
RUN /bin/bash -c 'source /home/mine/.homesick/repos/homeshick/homeshick.sh && homeshick clone -b mine260309/dotfiles && homeshick link -f -b dotfiles'
#RUN git clone https://github.com/VundleVim/Vundle.vim.git /home/mine/.vim/bundle/Vundle.vim && vim +PluginInstall +qall
# vim-plug
RUN /bin/bash -c 'curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim && vim +PlugInstall +qall'

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

CMD /bin/bash

