FROM fedora:latest
MAINTAINER Chris Byrd

RUN dnf clean all \
  && dnf update -v --debugsolver vim-minimal -y \
  && dnf install --best --allowerasing -y \
      automake \
      bash-completion \
      bison \
      bzip2 \
      ca-certificates \
      cppcheck \
      ctags \
      curl \
      dos2unix \
      flex \
      gcc \
      gcc-c++ \
      git \
      golang \
      golang-docs \
      gpg \
      jq \
      kernel-devel \
      libffi-devel \
      libtool \
      libyaml-devel \
      make \
      nodejs \
      openssh-clients \
      openssl-devel \
      patch \
      powerline \
      procps-ng \
      python3-pylint \
      readline-devel \
      rsync \
      samba-client \
      sqlite-devel \
      subversion \
      tar \
      task \
      the_silver_searcher \
      tmux \
      tmux-powerline \
      tree \
      unzip \
      which \
      wget \
      vim \
      zip \
      zlib \
      zlib-devel \
    && dnf clean all

RUN useradd -m dev \
  && echo 'dev:dev' | chpasswd \
  && echo 'root:root' | chpasswd \
  && usermod dev -a -G wheel

USER dev
WORKDIR /home/dev

RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 \
  && curl -v -sSL https://get.rvm.io | bash \
  && /home/dev/.rvm/bin/rvm install 2.4.1 \
  && /home/dev/.rvm/bin/rvm alias create default 2.4.1 \
  && /home/dev/.rvm/bin/rvm all do gem install --backtrace bundle \
  && /home/dev/.rvm/bin/rvm all do gem install --backtrace tmuxinator \
  && /home/dev/.rvm/bin/rvm all do gem install --backtrace rubocop \
  && /home/dev/.rvm/bin/rvm cleanup all \
  && dnf clean all

ENV EDITOR=vim SHELL=/bin/bash GOPATH=/home/dev/godev LC_CTYPE=C.UTF8 LC_ALL=C.UTF8 LD_LIBRARY_PATH=/usr/local/lib

# Setup desired directories, bash, and vim
RUN mkdir src \
  && mkdir godev \
  && mkdir .ssh \
  && git clone --depth=1 https://github.com/Bash-it/bash-it.git .bash_it \
  && .bash_it/install.sh \
  && echo "export TERM=screen-256color" >> .bashrc \
  && echo "export PATH=$GOPATH/bin:$PATH" >> .bashrc \
  && echo "source /home/dev/.rvm/scripts/rvm" >> .bashrc \
  && echo "source /usr/share/bash-completion/completions/git" >> .bashrc \
  && echo "alias vi=vim" >> .bashrc \
  && git clone https://github.com/VundleVim/Vundle.vim.git .vim/bundle/Vundle.vim \
  && git clone https://github.com/cabyrd/dot-files.git \
  && cp dot-files/.vimrc . \
  && cp dot-files/.tmux.conf . \
  && rm -rf dot-files \
  && vim +PluginInstall +qall

CMD ["/bin/bash"]
