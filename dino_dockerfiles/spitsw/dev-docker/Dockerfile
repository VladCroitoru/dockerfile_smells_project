FROM ubuntu:18.04
LABEL maintainer="Warren Spits <warren@spits.id.au>"
LABEL description="Preconfigured development environment"

ARG user="warren"
ARG fullname="Warren Spits"
ARG email="warren@spits.id.au"
ARG timezone="Australia/Melbourne"

RUN sed --in-place --regexp-extended "s/(\/\/)(archive\.ubuntu)/\1au.\2/" /etc/apt/sources.list \
  && rm -rf /var/lib/apt/lists/* && apt-get update

RUN apt-get install -y xz-utils
RUN apt-get install -y openssh-server tmux zsh curl man-db sudo iputils-ping locales \
	               tzdata mosh xsel xclip htop strace ltrace lsof dialog vim-common
RUN apt-get install -y aptitude software-properties-common
RUN echo 'docker.io docker.io/restart boolean true' | debconf-set-selections
RUN apt-get install -y docker.io docker-compose \
                       ruby2.5 ruby2.5-dev \
                       python3-pip python3 python \
                       build-essential cmake autoconf exuberant-ctags
RUN apt-get install -y ncurses-dev libsqlite3-dev tig
RUN update-alternatives --install /usr/bin/ruby ruby /usr/bin/ruby2.5 400

COPY ca-certificates/ /usr/local/share/ca-certificates/
RUN update-ca-certificates

RUN add-apt-repository ppa:longsleep/golang-backports && \
  apt-get update && apt-get install -y golang-go

RUN add-apt-repository ppa:neovim-ppa/unstable \
  && apt-get update && apt-get install -y neovim \
  && update-alternatives --install /usr/bin/vi vi /usr/bin/nvim 60 \
  && update-alternatives --install /usr/bin/vim vim /usr/bin/nvim 60 \
  && update-alternatives --install /usr/bin/editor editor /usr/bin/nvim 60

# Install dependencies for lastpass-cli
RUN apt-get update && apt-get install -y \
    openssl libcurl4-openssl-dev libxml2 libssl-dev libxml2-dev pinentry-curses

# Install git ppa for latest stable
RUN  add-apt-repository ppa:git-core/ppa \
  && apt-get update && apt-get install -y git

RUN mkdir /var/run/sshd
EXPOSE 22

RUN rm /etc/update-motd.d/*
RUN ln -sf /usr/share/zoneinfo/$timezone /etc/localtime

RUN apt-get install -y locales
COPY locale.gen /etc/
RUN locale-gen && update-locale LANG=en_AU.UTF-8

RUN adduser $user --disabled-password --shell /bin/zsh --gecos "$fullname,,,,$email" \
  && usermod $user -G sudo,users -a \
  && passwd -d $user

# Change the sudo config
RUN  perl -i -pe 's|(%sudo.*\s+)ALL$|$1NOPASSWD:ALL|g' /etc/sudoers \
  && echo 'Defaults env_keep = "http_proxy https_proxy ftp_proxy DISPLAY XAUTHORITY"' > /etc/sudoers.d/preserve_env¬

COPY home/ /home/$user/
RUN chown -R $user:$user /home/$user

USER $user

RUN git config --global user.name "$fullname" \
  && git config --global user.email "$email"

# Install oh-my-zsh
RUN umask g-w,o-w; git clone --depth 1 https://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
  && git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting \
  && git clone https://github.com/Treri/fzf-zsh.git ~/.oh-my-zsh/custom/plugins/fzf-zsh \
  && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
  && sed -i 's/^ZSH_THEME=.*/ZSH_THEME="blinks"/' ~/.zshrc \
  && perl -0pe 's/^(plugins=)\(.*\)/$1(gitfast gitignore ruby golang node rust docker zsh-syntax-highlighting fzf-zsh)/ms' -i ~/.zshrc
COPY zsh_custom/ /home/$user/.oh-my-zsh/custom

# install fzf, tpm, python neovim, vim plugin manager
RUN git clone https://github.com/junegunn/fzf.git ~/.fzf && ~/.fzf/install --bin \
  && ln -s ~/.fzf ~/.oh-my-zsh/custom/plugins/fzf \
  && git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm \
  && ~/.tmux/plugins/tpm/bin/install_plugins \
  && pip3 install setuptools && pip3 install neovim pynvim \
  && curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# install some useful python built tools
RUN pip3 install aws

# Install nvm with node and npm
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash \
    && NVM_DIR=/home/$user/.nvm && . $NVM_DIR/nvm.sh \
    && nvm install --lts node \
    && npm config set cafile /etc/ssl/certs/ca-certificates.crt \
    && npm install -g --upgrade npm
RUN NVM_DIR=/home/$user/.nvm && . $NVM_DIR/nvm.sh \
    && npm install -g yarn eslint_d javascript-typescript-langserver import-js \
    && mkdir -p /home/$user/.config/coc/extensions && cd /home/$user/.config/coc/extensions \
    && echo '{"dependencies":{}}' > package.json \
    && npm i coc-json coc-git coc-rust-analyzer coc-snippets coc-tsserver coc-highlight coc-pairs --no-shrinkwrap

# Install rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --no-modify-path \
  && /home/$user/.cargo/bin/rustup component add rust-src \
  && /home/$user/.cargo/bin/rustup component add rust-docs \
  && /home/$user/.cargo/bin/rustup component add clippy \
  && /home/$user/.cargo/bin/cargo install cargo-watch cargo-edit ripgrep

RUN git clone https://github.com/rust-analyzer/rust-analyzer ~/build/rust-analyzer \
  && cd ~/build/rust-analyzer && ~/.cargo/bin/cargo install-ra --server

ARG GOPATH=/home/$user/go
RUN (echo export GOPATH=$GOPATH \
  && echo export PATH=\$GOPATH/bin:/home/$user/.cargo/bin:/home/$user/.local/bin:\$PATH \
  && echo export CDPATH=.:$GOPATH/src \
  && echo export FZF_DEFAULT_COMMAND=\'rg --files --no-ignore-vcs --hidden' \
  && echo export FZF_TMUX=1 ) >> ~/.zshrc

RUN nvim --headless +PlugInstall +UpdateRemotePlugins +qa \
  && nvim --headless +GoInstallBinaries +qa

RUN go get -v github.com/github/hub

# Build lastpass-cli
RUN git clone -b v1.3.3 https://github.com/lastpass/lastpass-cli.git ~/build/lastpass-cli \
  && cd ~/build/lastpass-cli && make

USER root

# Install lastpass-cli
RUN cd /home/$user/build/lastpass-cli && make PREFIX=/usr/local install

# Fix permissions
RUN chown -R $user:$user /home/$user/.oh-my-zsh/custom

CMD    ["/usr/sbin/sshd", "-D"]
