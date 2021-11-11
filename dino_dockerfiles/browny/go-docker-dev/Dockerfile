FROM golang:1.6.2
MAINTAINER Browny Lin

ADD fs/ /

# install pagkages
RUN apt-get update                                                      && \
    apt-get install -y ncurses-dev exuberant-ctags unzip sudo           && \
    cd /tmp                                                             && \
# build and install vim
    git clone https://github.com/vim/vim.git                            && \
    cd vim                                                              && \
    ./configure --with-features=huge                                       \
        --enable-gui=no --without-x --prefix=/usr                       && \
    make VIMRUNTIMEDIR=/usr/share/vim/vim74                             && \
    make install                                                        && \
# get go tools
    go get golang.org/x/tools/cmd/godoc                                 && \
    go get github.com/nsf/gocode                                        && \
    go get golang.org/x/tools/cmd/goimports                             && \
    go get github.com/rogpeppe/godef                                    && \
    go get golang.org/x/tools/cmd/oracle                                && \
    go get golang.org/x/tools/cmd/gorename                              && \
    go get github.com/golang/lint/golint                                && \
    go get github.com/kisielk/errcheck                                  && \
    go get github.com/jstemmer/gotags                                   && \
    go get github.com/tools/godep                                       && \
    go get github.com/mjibson/esc                                       && \
    mv /go/bin/* /usr/local/go/bin                                      && \
	# add dev user
    adduser dev --disabled-password --gecos ""                          && \
    echo "ALL            ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers     && \
    chown -R dev:dev /home/dev /go /var/log                             && \
# cleanup
    rm -rf /go/src/* /go/pkg                                            && \
    apt-get remove -y ncurses-dev                                       && \
    apt-get autoremove -y                                               && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

Run go get github.com/stretchr/testify

# install tmux
RUN echo "deb http://archive.ubuntu.com/ubuntu/ precise main universe" >> /etc/apt/sources.list
RUN apt-get -q -y update
RUN apt-get install -y tmux

USER dev
ENV HOME /home/dev

# install vim plugins
RUN mkdir -p ~/.vim/bundle                                              && \
    cd  ~/.vim/bundle                                                   && \
    git clone --depth 1 https://github.com/gmarik/Vundle.vim.git        && \
    git clone --depth 1 https://github.com/fatih/vim-go.git             && \
    git clone --depth 1 https://github.com/kien/ctrlp.vim               && \
    git clone --depth 1 https://github.com/fholgado/minibufexpl.vim     && \
    git clone --depth 1 https://github.com/tpope/vim-fugitive           && \
    vim +PluginInstall +qall                                            && \
# cleanup
    rm -rf Vundle.vim/.git vim-go/.git kien/ctrlp.vim/.git fholgado/minibufexpl.vim/.git tpope/vim-fugitive/.git
