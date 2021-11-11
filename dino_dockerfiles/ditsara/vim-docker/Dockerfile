FROM alpine:3.7
MAINTAINER Dan Itsara <dan@glazziq.com>

RUN apk --update --no-cache add \
    bash \
    ctags \
    curl \
    git \
    less \
    xclip \
    ncurses-terminfo \
    neovim \
    neovim-doc

RUN \
  # load bash-it and set aliases
  git clone --depth=1 https://github.com/Bash-it/bash-it.git ~/.bash_it && \
  ~/.bash_it/install.sh --silent --no-modify-config && \
  ln -s ~/.bash_it/aliases/available/git.aliases.bash ~/.bash_it/enabled/150---git.aliases.bash && \
  ln -s ~/.bash_it/aliases/available/vim.aliases.bash ~/.bash_it/enabled/150---vim.aliases.bash && \
  # set default shell to bash
  sed -i 's/ash/bash/g' /etc/passwd && \
  mkdir /app && \
  # install neovim plugin manager
  curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim && \
  # build, install universal-ctags
  git clone http://github.com/universal-ctags/ctags.git ~/ctags && \
  cd ~/ctags && \
  apk --update --no-cache add --virtual build-deps \
    autoconf make gcc automake musl-dev && \
  ./autogen.sh && \
  ./configure --program-prefix=u && \
  make && make install && \
  # cleanup
  cd ~ && rm -rf ctags && \
  apk del build-deps

# add config files and install neovim plugins; separate layer so we don't need
# to re-build everything when we change plugins or add files to home directory
ADD home /root
RUN nvim -E -u NONE -S ~/.config/nvim/init.vim +PlugInstall +qall > /dev/null || true

WORKDIR /app
ENV DISPLAY=:0
CMD nvim
