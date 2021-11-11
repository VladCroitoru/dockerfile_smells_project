#
# Copyright 2015 1&1 Internet AG, http://1und1.de . All rights reserved. Licensed under the Apache v2 License.
#

FROM debian:8.1

MAINTAINER Joachim Lusiardi <joachim.lusiardi@1und1.de>

ENV HOME=/home/godev
ENV GOVERSION=1.4.2

# install all packages from repos
RUN \
	apt-get update -y ;\
	apt-get install -y \
		vim-nox \
		curl \
		git \
		tmux

# add user & prepare dirs
RUN \
	useradd --create-home --shell /bin/bash godev ; \
	mkdir -p $HOME/go/src $HOME/go/bin $HOME/bin ; \
	chmod -R 777 $HOME/go ; 

# 
COPY vimrc /home/godev/vimrc
RUN \
	mv /home/godev/vimrc /home/godev/.vimrc


# configure vim to support go dev
RUN \
	mkdir -p $HOME/.vim/autoload $HOME/.vim/bundle && \
	curl -LSso $HOME/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim ; \
	git clone https://github.com/fatih/vim-go.git $HOME/.vim/bundle/vim-go ; 

# install go
RUN \
	curl https://storage.googleapis.com/golang/go$GOVERSION.linux-amd64.tar.gz > /tmp/go$GOVERSION.linux-amd64.tar.gz ; \
	tar -C $HOME/bin/ -xzf /tmp/go$GOVERSION.linux-amd64.tar.gz ; \
	echo "export PATH=\"$HOME/bin/go/bin:\$PATH\"" >> $HOME/.bashrc ; \
	echo "export GOPATH=$HOME/go" >> $HOME/.bashrc ; \
	echo "export GOROOT=$HOME/bin/go" >> $HOME/.bashrc ; 

# install neocomplete
RUN \
	git clone https://github.com/Shougo/neocomplete.vim.git /tmp/neocomplete ; \
	mkdir -p $HOME/.vim/autoload ; \
	mkdir -p $HOME/.vim/plugin ; \
	cp -a /tmp/neocomplete/autoload/* $HOME/.vim/autoload ; \
	cp -a /tmp/neocomplete/plugin/* $HOME/.vim/plugin

# install numbers.vim
RUN \
	git clone https://github.com/myusuf3/numbers.vim.git $HOME/.vim/bundle/numbers

# add custom inputrc
COPY inputrc /etc/inputrc

# make bash nicer
COPY bash_customize $HOME/.bash_customize
RUN \
	curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash > $HOME/.git-completion.bash; \
	echo "source $HOME/.git-completion.bash" >> $HOME/.bashrc; \
	echo "source $HOME/.bash_customize" >> $HOME/.bashrc

USER godev

VOLUME ["/home/godev/go"]

WORKDIR /home/godev/go/src
EXPOSE 6060
COPY start.sh /start.sh
CMD /start.sh
