FROM debian:stretch-slim

ARG DEBIAN_FRONTEND=noninteractive

#Update sources
RUN apt-get -y update

#Install base packages
#TODO: maybe split into domain-specific dependecies
RUN apt-get install -y --no-install-recommends \
    sudo \
    lsb-release \
    git \
    wget \
    ca-certificates \
    curl \
    locate \
    htop \
    exuberant-ctags \
    ngrep \
    grc \
    unzip \
    bash-completion \
    man \
    less \
    make \
    aspell \
    ncdu \
    locales

RUN echo "pt_PT.UTF-8 UTF-8" >> /etc/locale.gen && \
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen pt_PT.UTF-8 en_US.UTF-8

## Add USER
ARG USER_NAME=dot
ARG USER_PASSWORD=files
ARG USER_ID=1000
ENV USER_PUBLIC_KEY=
RUN useradd -u ${USER_ID} -m -s /bin/bash -U ${USER_NAME} && \
    echo "${USER_NAME}:${USER_PASSWORD}"|chpasswd && \
    adduser ${USER_NAME} sudo && \
    echo ${USER_NAME}' ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
#rando password: `openssl rand -base64 32`

USER ${USER_NAME}
WORKDIR /home/${USER_NAME}

RUN mkdir -m 700 $HOME/.ssh
#Adding my known hosts (e.g. Github)
ADD ./configuration/ssh/known_hosts $HOME/.ssh/known_hosts

#Cherry picking binaries to optimize docker build cache usage

#Install git
#ARG GIT_VERSION=
#ADD ./bin/install-git .dotfiles/bin/
#RUN .dotfiles/bin/install-git $GIT_VERSION

#Install tig (for git repository browsing)
ARG TIG_VERSION=
ADD ./bin/install-tig .dotfiles/bin/
RUN .dotfiles/bin/install-tig $TIG_VERSION

#Install tmux
ARG TMUX_VERSION=
ADD ./bin/install-tmux .dotfiles/bin/
RUN .dotfiles/bin/install-tmux $TMUX_VERSION

#Install Python
ARG PYTHON_VERSION=
ADD ./bin/install-python .dotfiles/bin/
RUN .dotfiles/bin/install-python $PYTHON_VERSION

#Install Ruby
ARG RUBY_VERSION=
ADD ./bin/install-ruby .dotfiles/bin/
RUN .dotfiles/bin/install-ruby $RUBY_VERSION

#Install Go
ARG GO_VERSION=
ADD ./bin/install-go .dotfiles/bin/
RUN .dotfiles/bin/install-go $GO_VERSION

#Install git-hooks
ARG GIT_HOOKS_VERSION=
ADD ./bin/install-git-hooks .dotfiles/bin/
RUN .dotfiles/bin/install-git-hooks $GIT_HOOKS_VERSION

#Install npm
ARG NODE_VERSION=
ADD ./bin/install-node .dotfiles/bin/
RUN .dotfiles/bin/install-node $NODE_VERSION

#Install Vim using previously python/ruby installation
ARG VIM_VERSION=
ADD ./bin/install-vim .dotfiles/bin/
RUN bash -c 'eval "$($HOME/.rbenv/bin/rbenv init -)" && \
             eval "$($HOME/.pyenv/bin/pyenv init -)" && \
             .dotfiles/bin/install-vim $VIM_VERSION'

ADD ./bin/install-zsh .dotfiles/bin/
RUN .dotfiles/bin/install-zsh

ARG DEFAULT_SHELL=zsh
RUN sudo chsh -s $(which $DEFAULT_SHELL) $USER_NAME

## dotfiles
ADD ./bin .dotfiles/bin
ADD ./configuration .dotfiles/configuration
RUN sudo chown -R $USER_NAME:$USER_NAME .dotfiles/configuration

#Ensure dotfiles symlinks
RUN .dotfiles/bin/dotfiles-symlinks -f

RUN vim +PlugInstall +qall

RUN  zsh -c "export TERM=xterm;\
             export LANG=en_US.UTF-8;\
             export ZPLUG_LOADFILE=~/.zsh/packages.zsh; \
             source ~/.zplug/init.zsh; \
             zplug install;"

USER root
ENV USER_NAME=$USER_NAME

#Now that we're done, let's force sudo to ask password
RUN sed -i 's/NOPASSWD://' /etc/sudoers && chpasswd ${USER_NAME}:${USER_PASSWORD}

CMD ["/usr/bin/zsh"]

USER $USER_NAME
ENV HOME /home/$USER_NAME

WORKDIR /workspaces
