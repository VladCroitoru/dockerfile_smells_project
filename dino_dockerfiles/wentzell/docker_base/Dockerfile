FROM ubuntu:focal

## Set up additional packages
WORKDIR /tmp
ADD pkglst /tmp
RUN yes | unminimize && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends $(cat pkglst) && \
    apt-get autoremove --purge -y && \
    apt-get autoclean -y && \
    rm -rf /var/cache/apt/* /var/lib/apt/lists/*

# Set the locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Set up user docker
ARG NB_USER=docker
ARG NB_UID=1000
RUN useradd -u $NB_UID -m $NB_USER && \
    echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER $NB_USER
WORKDIR /home/$NB_USER

# Set up config files
RUN git clone --recursive http://github.com/Wentzell/dotfiles
WORKDIR /home/$NB_USER/dotfiles
RUN git checkout ubuntu
RUN ./link.sh
WORKDIR /home/$NB_USER
RUN git clone http://github.com/altercation/vim-colors-solarized /home/$NB_USER/.vim/bundle/vim-colors-solarized
RUN vim +PlugInstall +qall &> /dev/null

CMD ["/usr/bin/zsh", "-l"]
