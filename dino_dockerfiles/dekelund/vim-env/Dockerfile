# This Dockerfile installs vim with janus, it does also include some other
# vim plugins. As shell it defaults to zsh, and uses tmux as entrypoint,
# which starts up vim and shell.
#
# Powerline is a prerequisite for themes and plugins used by tmux, zsh and vim
# in this setup, https://github.com/powerline/fonts/tree/master/LiberationMono
FROM golang:1.7-wheezy
MAINTAINER Daniel Ekelund


# Setup OS and tools
ENV TERM=screen-256color

RUN echo "deb http://http.debian.net/debian wheezy-backports main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y ack ctags git ruby rake python git legit tmux zsh build-essential python-dev python3-dev libclang-dev zsh less
RUN apt-get -t wheezy-backports install -y vim-nox vim-common cmake python-pip ipython


# Install Janus Vim Environment
RUN curl -L https://bit.ly/janus-bootstrap | bash
RUN mkdir -p /repo /root/.janus


# Install Extra Plugins
WORKDIR /root/.janus

RUN git clone --recursive https://github.com/chrisbra/csv.vim
RUN git clone --recursive https://github.com/gregsexton/gitv
RUN git clone --recursive https://github.com/scrooloose/syntastic.git syntastic
RUN git clone --recursive https://github.com/SirVer/ultisnips
RUN git clone --recursive https://github.com/Shougo/unite.vim
RUN git clone --recursive https://github.com/bling/vim-airline
RUN git clone --recursive git://github.com/altercation/vim-colors-solarized.git vim-colors-solarized
RUN git clone --recursive git://github.com/justincampbell/vim-eighties.git vim-eighties
RUN git clone --recursive https://github.com/fatih/vim-go.git vim-go
RUN git clone --recursive https://github.com/honza/vim-snippets.git vim-snippets
RUN git clone --recursive https://github.com/jmcantrell/vim-virtualenv
RUN git clone --recursive https://github.com/Shougo/vimproc.vim
RUN git clone --recursive https://github.com/benmills/vimux-golang
RUN git clone --recursive https://github.com/jgors/vimux-ipy
RUN git clone --recursive https://github.com/benmills/vimux
RUN git clone --recursive https://github.com/ross/requests-futures
# RUN git clone --recursive https://github.com/tpope/vim-dispatch


# Install You Complete Me
RUN git clone --recursive https://github.com/valloric/youcompleteme
RUN git clone --recursive https://github.com/Valloric/ycmd

WORKDIR /root/.janus/youcompleteme
RUN ./install.py --gocode-completer


# Setup golang tools (List copied from: mbrt/golang-vim-dev
RUN go get golang.org/x/tools/cmd/godoc
RUN go get github.com/nsf/gocode
RUN go get golang.org/x/tools/cmd/goimports
RUN go get github.com/rogpeppe/godef
RUN go get golang.org/x/tools/cmd/guru
RUN go get golang.org/x/tools/cmd/gorename
RUN go get github.com/golang/lint/golint
RUN go get github.com/kisielk/errcheck
RUN go get github.com/jstemmer/gotags
RUN go get github.com/tools/godep
RUN go get github.com/alecthomas/gometalinter
RUN go get github.com/zmb3/gogetdoc
RUN go get github.com/klauspost/asmfmt/cmd/asmfmt
RUN go get github.com/fatih/motion
RUN go get github.com/josharian/impl

# Setup BDD tools
RUN go get gomate.io/gomate
RUN go install gomate.io/gomate

# Setup debuggers
RUN go get github.com/derekparker/delve/cmd/dlv

# Setup customisation of vim and plugins
COPY .vimrc.after /root/.vimrc.after
COPY .vimrc.before /root/.vimrc.before


# Install oh-my-zsh, use local version of install script
COPY install-oh-my-zsh.sh /opt/install-oh-my-zsh.sh
RUN zsh -c /opt/install-oh-my-zsh.sh

COPY ./.zshrc /root/.zshrc
RUN pip install powerline-status

# Add script to be used as entrypoint
COPY ./.tmux.conf /root/.tmux.conf
COPY start.sh /opt/start.sh

# Vim configuration file to be user by host
RUN mkdir -p /root/hostconfig
RUN touch /root/hostconfig/vimrc

# Setup Language Environtment
ENV LANG="C.UTF-8"
ENV LC_COLLATE="C.UTF-8"
ENV LC_CTYPE="C.UTF-8"
ENV LC_MESSAGES="C.UTF-8"
ENV LC_MONETARY="C.UTF-8"
ENV LC_NUMERIC="C.UTF-8"
ENV LC_TIME="C.UTF-8"

RUN apt-get install -y watch

# Start the container
WORKDIR /repo
ENTRYPOINT ["/opt/start.sh"]
CMD ["default"]
