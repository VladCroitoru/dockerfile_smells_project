FROM ubuntu:latest

MAINTAINER Serge Ovchinnikov (sovchinn@gmail.com)

ENV HOME /root

# Install core package
RUN apt-get update -y && apt-get install -y \
    git \
    make \
    zsh \
    curl 

# Install Neovim
RUN apt-get install -y \
    software-properties-common &&\
    add-apt-repository ppa:neovim-ppa/stable &&\
    apt-get update &&\
    apt-get install -y \
    neovim \
    python-dev \
    python-pip \ 
    python3-dev \
    python3-pip &&\
    pip3 install neovim 

# Cleanup
RUN apt-get autoremove -y &&\
    apt-get clean -y &&\
    rm -rf /var/lib/apt/lists/*

# Install Go
RUN curl -O https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz &&\
    tar -xf go1.9.linux-amd64.tar.gz &&\
    mv go /usr/local &&\
    rm go1.9.linux-amd64.tar.gz 

# Install dot files
RUN git clone --recursive https://github.com/sovchinn/dot.git $HOME/dot 
WORKDIR $HOME/dot
RUN make

# Install plugins
RUN nvim -c 'PlugInstall' -c 'UpdateRemotePlugins' -c 'qa!'

# Install Go(lang) binaries
RUN nvim +GoInstallBinaries +qall; exit 0
RUN /usr/local/go/bin/go get -u github.com/nsf/gocode

WORKDIR $HOME
ENV SHELL /bin/zsh

CMD ["zsh"] 
