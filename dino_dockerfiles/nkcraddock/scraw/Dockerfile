FROM debian:stable


## install all that good stuff
RUN apt-get update \
  && apt-get install -y \
  apt-utils \
  build-essential \
  curl \
  git \
  jq \
  mercurial \
  silversearcher-ag \
  wget \
  vim-gtk \
  tmux \
  tmate \
  sudo \
  autotools-dev \
  autoconf \ 
  pkg-config \
  locales \
  httpie \
  && dpkg-reconfigure --frontend=noninteractive locales \
  && echo "Installing ctags" \
  && git clone -q --depth=1 https://github.com/universal-ctags/ctags.git /tmp/ctags \
  && cd /tmp/ctags \
  && ./autogen.sh \
  && ./configure \
  && make \
  && sudo make install \
  && cd - \
  && echo "Cleaning up" \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set up scripts and root home
WORKDIR /root/dev

COPY home/bin/vim-plug /root/bin/vim-plug
COPY home/.vim-plugins /root/.vim-plugins

RUN $HOME/bin/vim-plug

COPY home/ /root/

RUN /root/bin/install-node

# Setting up YouCompleteMe
RUN apt-get update \
  && apt install -y cmake python3-dev \
  && cd ~/.vim/bundle/youcompleteme && ./install.sh && cd - \
  && echo "Cleaning up" \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" \
    | tee /etc/apt/sources.list.d/mongodb-org-4.0.list \
  && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \
    --recv 9DA31620334BD75D9DCB49F368818C72E52529D4 \
  && apt update -y\
  && apt install -y mongodb-org-shell \
  && echo "Cleaning up" \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8   

CMD ["/bin/bash"]

