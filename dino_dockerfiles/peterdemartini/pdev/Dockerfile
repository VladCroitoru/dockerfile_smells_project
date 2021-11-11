FROM alpine:edge
MAINTAINER Peter DeMartini (https://github.com/peterdemartini)

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root
ENV XDG_CONFIG_HOME /usr/local/etc
ENV XDG_DATA_HOME /usr/local/share
ENV XDG_CACHE_HOME /usr/local/cache

# build deps
RUN apk add --update-cache --virtual build-deps --no-cache \
    curl g++ libtool libuv upower \
    ncurses ncurses-dev ncurses-libs ncurses-terminfo \
    linux-headers lua5.3-dev lua-sec \
    m4 unzip ctags \
    alpine-sdk build-base \
    openssh-client ca-certificates \
    tzdata libstdc++ \
    fontconfig musl-dev

# tools
RUN apk add --update-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
    fish bash less tmux \
    clang go git \
    nodejs yarn \
    libtermkey neovim neovim-doc \
    python-dev python3-dev python3 \
    the_silver_searcher

# ruby
RUN apk add --update-cache \
    ruby ruby-dev ruby-irb ruby-rake ruby-io-console ruby-bigdecimal ruby-json ruby-bundler \
    && echo 'gem: --no-document' > /etc/gemrc

# Clean the cache
RUN rm -rf /var/cache/apk/*

# ENV CMAKE_EXTRA_FLAGS=-DENABLE_JEMALLOC=OFF

# fonts
RUN mkdir -p /usr/local/share/fonts \
  && cd /usr/local/share/fonts \
  && curl --silent -fLo "Fura Code Regular Nerd Font Complete.otf" https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/FiraCode/Regular/complete/Fura%20Code%20Regular%20Nerd%20Font%20Complete.otf \
  && fc-cache -fv

# git
COPY gitconfig $HOME/.gitconfig
COPY gitignore_global $HOME/.gitignore_global
RUN apk add --update-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/ \
    hub

# go
ENV GOPATH $XDG_DATA_HOME/go
ENV GOBIN $XDG_DATA_HOME/go/bin
ENV PATH "$PATH:$GOBIN"

# ssh
COPY ssh $HOME/.ssh
RUN ssh-keyscan github.com > $HOME/.ssh/known_hosts

# colors
COPY xterm-256color-italic.terminfo $XDG_CONFIG_HOME/xterm-256color-italic.terminfo
ENV TERM xterm-256color-italic
RUN tic $XDG_CONFIG_HOME/xterm-256color-italic.terminfo
# RUN curl -fsSL https://raw.githubusercontent.com/JohnMorales/dotfiles/master/colors/24-bit-color.sh | bash

# tmux config
COPY tmux-theme.conf $HOME/.tmux-theme.conf
COPY tmux.conf $HOME/.tmux.conf
RUN git clone https://github.com/tmux-plugins/tpm $HOME/.tmux/plugins/tpm \
  && $HOME/.tmux/plugins/tpm/bin/install_plugins

# node
ENV NPM_CONFIG_LOGLEVEL error
RUN yarn global add eslint prettier && yarn cache clean

# neovim
RUN pip3 install neovim
RUN gem install neovim

ENV NVIM_PYTHON_LOG_FILE /tmp/nvim_log

COPY ctags $HOME/.ctags
COPY config/nvim $XDG_CONFIG_HOME/nvim

RUN git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf \
 && ~/.fzf/install --bin

RUN curl -sfLo $XDG_CONFIG_HOME/nvim/autoload/plug.vim --create-dirs \
  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim \
  && nvim --headless +PlugInstall +qa &> /dev/null \
  && nvim --headless +UpdateRemotePlugins +qa &> /dev/null

RUN mkdir -p $XDG_CONFIG_HOME/nvim/spell \
  && curl --silent ftp://ftp.vim.org/pub/vim/runtime/spell/en.utf-8.spl -o $XDG_CONFIG_HOME/nvim/spell/en.utf-8.spl

RUN mkdir -p $XDG_CONFIG_HOME/nvim/shada && touch $XDG_CONFIG_HOME/nvim/shada/main.shada

ENV PATH "$PATH:$HOME/.fzf/bin"

# fish
COPY config/fish $XDG_CONFIG_HOME/fish
COPY config/omf $XDG_CONFIG_HOME/omf
RUN curl --silent -L http://get.oh-my.fish > /tmp/omf-install \
  && fish /tmp/omf-install --noninteractive --path=/usr/local/bin/omf --config=$XDG_CONFIG_HOME/omf \
  && rm /tmp/omf-install

ENV SHELL /usr/bin/fish

RUN fish -c "omf install"

COPY bin /usr/local/bin

RUN chmod -R 777 /usr/local

WORKDIR /workdir

CMD [ "/usr/bin/fish" ]
