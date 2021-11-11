FROM ubuntu:latest

# environment variables
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y vim git wget fontconfig curl exuberant-ctags  

RUN useradd dev && \
    echo "ALL            ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    cp /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && \
    dpkg-reconfigure locales && \
    locale-gen en_US.UTF-8 && \
    /usr/sbin/update-locale LANG=en_US.UTF-8

WORKDIR /home/dev
ENV HOME /home/dev
ENV LC_ALL en_US.UTF-8

RUN chown -R dev:dev $HOME
USER dev

# setup pathogen vim plugin manager
RUN mkdir -p $HOME/.vim/autoload $HOME/.vim/bundle && \
    wget -P $HOME/.vim/autoload https://tpo.pe/pathogen.vim

COPY vimrc $HOME/.vimrc

RUN mkdir -p ~/.vim/autoload ~/.vim/bundle && \
  curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim && \
# Install vim plugins
  cd ~/.vim/bundle && \
  git clone git://github.com/tpope/vim-sensible.git && \
  git clone https://github.com/scrooloose/nerdtree.git && \
  git clone https://github.com/vim-airline/vim-airline.git && \
  git clone https://github.com/vim-airline/vim-airline-themes.git && \
  git clone https://github.com/kien/ctrlp.vim && \
  git clone https://github.com/scrooloose/syntastic && \
  git clone https://github.com/ternjs/tern_for_vim && \
  git clone https://github.com/tpope/vim-fugitive && \
  git clone https://github.com/tpope/vim-surround && \
  git clone https://github.com/pangloss/vim-javascript && \
  git clone https://github.com/tpope/vim-rails && \
  git clone https://github.com/vim-ruby/vim-ruby && \
  git clone https://github.com/elzr/vim-json && \
  git clone https://github.com/elixir-lang/vim-elixir && \
  git clone https://github.com/moll/vim-node && \
  git clone https://github.com/airblade/vim-gitgutter && \
  git clone https://github.com/sirver/ultisnips.git && \
  git clone https://github.com/honza/vim-snippets.git && \
  git clone https://github.com/majutsushi/tagbar && \
  git clone https://github.com/xolox/vim-easytags && \
  git clone https://github.com/xolox/vim-misc && \
  git clone https://github.com/ekalinin/Dockerfile.vim && \
  git clone https://github.com/vim-scripts/vim-auto-save && \
# Color schemes
  git clone https://github.com/sjl/badwolf.git && \
  git clone https://github.com/nanotech/jellybeans.vim.git

CMD vim
