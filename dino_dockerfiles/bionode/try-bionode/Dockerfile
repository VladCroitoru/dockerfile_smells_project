# Try Bionode
#
# VERSION               1.0.0

FROM ubuntu:15.10
MAINTAINER Bruno Vieira <mail@bmpvieira.com>

LABEL Description="For try.bionode.io workshop" Version="1.0.0"

# Fix locales, otherwise Fish will give 'Wide character 57520 has no narrow representation'
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install Ubuntu packages
RUN apt-get update
RUN apt-get install -y build-essential ncurses-dev libncurses5-dev gettext autoconf automake m4 curl vim git npm python ruby

# Install Node.js
RUN npm install -g n
RUN n 0.10.40

# From mafintosh/docker-adventure-time to make this work
RUN npm install -g expose-fs@1.2.0 streaming-format@1.1.0
ADD run-container /run-container
WORKDIR /root
ENTRYPOINT /run-container
ADD welcome.txt /

# Install latest Fish shell
RUN git clone https://github.com/fish-shell/fish-shell.git ;\
  cd fish-shell ;\
  autoconf ;\
  ./configure ;\
  make ;\
  make install ;\
  cd .. ;\
  rm -r fish-shell
RUN curl -L https://github.com/oh-my-fish/oh-my-fish/raw/master/bin/install | fish
RUN fish -c 'omf install agnoster; omf theme agnoster'
RUN echo 'set fish_greeting ""' >> ~/.config/fish/config.fish 

# Install Bionode, Dat and JSON handling tool
RUN npm install -g bionode dat json

# Install Homebrew Linux and Bioinformatics packages
RUN ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/linuxbrew/go/install | grep -v 'run this as root')" < /dev/null
RUN echo 'export PATH="$HOME/.linuxbrew/bin:$PATH" \n\
export MANPATH="$HOME/.linuxbrew/share/man:$MANPATH" \n\
export INFOPATH="$HOME/.linuxbrew/share/info:$INFOPATH"' >> ~/.bashrc
RUN echo 'set -x PATH $PATH "$HOME/.linuxbrew/bin" \n\
set -x MANPATH $MANPATH "$HOME/.linuxbrew/share/man" \n\
set -x INFOPATH $INFOPATH "$HOME/.linuxbrew/share/info"' >> ~/.config/fish/config.fish
RUN fish -c 'brew tap homebrew/science'
RUN fish -c 'brew install bwa samtools'
RUN mkdir /root-dotconfigs
RUN fish -c 'cp -r /root/.* /root-dotconfigs'
