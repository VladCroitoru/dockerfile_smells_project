FROM ubuntu:16.04
MAINTAINER Ara Hacopian <arahacopian@gmail.com>
WORKDIR /tmp

# Start by changing the apt output, as stolen from Discourse's Dockerfiles.
RUN echo "debconf debconf/frontend select Teletype" | debconf-set-selections

RUN \
  apt-get update && apt-get -y install \
  ack-grep \
  bash \
  build-essential \
  ctags \
  curl \
  direnv \
  git \
  locales \
  man \
  openssh-client \
  openssh-server \
  openssl \
  ruby \
  sudo \
  tmux \
  vim \
  wget &&\
  apt-get -q clean &&\
  rm -rf /tmp/* /var/tmp/*

RUN gem install github-auth

# Install and setup wemux
RUN \
  git clone git://github.com/zolrath/wemux.git /usr/local/share/wemux &&\
  ln -s /usr/local/share/wemux/wemux /usr/local/bin/wemux &&\
  mkdir -p /usr/local/etc &&\
  cp /usr/local/share/wemux/wemux.conf.example /usr/local/etc/wemux.conf &&\
  echo "host_list=(dev)" >> /usr/local/etc/wemux.conf

# Set up SSH. We set up SSH forwarding so that transactions like git pushes
# from the container happen magically.
RUN \
  mkdir -p /var/run/sshd &&\
  echo "AllowAgentForwarding yes" >> /etc/ssh/sshd_config

# Fix for occasional errors in perl stuff (git, ack) saying that locale
# vars aren't set.

ENV LANG=en_US
RUN \
  locale-gen $LANG $LANG.UTF-8 && \
  sed -i -e "s/# $LANG.*/$LANG.UTF-8 UTF-8/" /etc/locale.gen && \
  dpkg-reconfigure --frontend=noninteractive locales && \
  update-locale LANG=$LANG

# Install ruby-install and chruby and gems
RUN \
  wget -O ruby-install-0.6.0.tar.gz https://github.com/postmodern/ruby-install/archive/v0.6.0.tar.gz &&\
  tar -xzvf ruby-install-0.6.0.tar.gz &&\
  cd ruby-install-0.6.0/ &&\
  make install &&\
  wget -O chruby-0.3.9.tar.gz https://github.com/postmodern/chruby/archive/v0.3.9.tar.gz &&\
  tar -xzvf chruby-0.3.9.tar.gz &&\
  cd chruby-0.3.9/ &&\
  make install &&\
  ./scripts/setup.sh &&\
  rm -rf /tmp/*

# Add docker arg to define which github user we should pull config from
# TODO: accomodate github users that do not have ahacop's exact
# dotfiles/vim setup
ARG userconfig=ahacop

# Add dev user
RUN \
  useradd dev -d /home/dev -m -s /bin/bash &&\
  adduser dev sudo && \
  echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER dev

# Install ruby via ruby-install
RUN \
  ruby-install --cleanup ruby &&\
  /bin/bash -c "source /usr/local/share/chruby/chruby.sh && chruby ruby && gem install homesick git-duet -N"

# Config dev user environment with github user's dotfiles/dotvim
RUN \
  /bin/bash -c "source /usr/local/share/chruby/chruby.sh && chruby ruby && homesick clone $userconfig/dotfiles && homesick link --force dotfiles" &&\
  git clone git://github.com/$userconfig/dotvim.git ~/.vim &&\
  ln -s ~/.vim/vimrc ~/.vimrc &&\
  cd ~/.vim && \
  git submodule init &&\
  git submodule update

# Expose SSH
EXPOSE 22

ADD ssh_key_adder.rb /home/dev/ssh_key_adder.rb

# Install the SSH keys of ENV-configured GitHub users before running the SSH
# server process. See README for SSH instructions.
CMD /home/dev/ssh_key_adder.rb && sudo /usr/sbin/sshd -D
