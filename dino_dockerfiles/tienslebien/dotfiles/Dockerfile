FROM debian:latest

MAINTAINER Tienslebien <etienne@crombez.info>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y vim-nox zsh git most

# Install oh-my-zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh &&\
    git clone git@github.com:zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions &&\
    git clone git://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting

ADD dotfiles/zshrc        ~/.zshrc
ADD dotfiles/my.zsh-theme ~/.oh-my-zsh/custom/my.zsh-theme
ADD dotfiles/gitconfig    ~/.gitconfig
ADD dotfiles/vimrc        ~/.vimrc
ADD dotfiles/vim          ~/.vim

RUN mkdir -p ~/.vim/bundle &&\
    git clone git://github.com/Shougo/neobundle.vim.git ~/.vim/bundle/neobundle.vim &&\
    ~/.vim/bundle/neobundle.vim/bin/neoinstall

ENTRYPOINT /bin/zsh
