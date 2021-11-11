FROM ruby:2.2.3

# Install dependencies & clean up
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    apt-transport-https \
    locales \
    ssh \
    zsh \
    vim \
    git \
    tmux \
    less \
    silversearcher-ag \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Change shell for build
RUN rm /bin/sh && ln -s /bin/zsh /bin/sh

# UTF-8
RUN cp /usr/share/zoneinfo/Canada/Eastern /etc/localtime \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && /usr/sbin/locale-gen \
    && /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install docker & docker-compose
ENV DOCKER_VERSION 1.8.2
ENV DOCKER_COMPOSE_VERSION 1.4.2
RUN curl -fLo /usr/local/bin/docker \
    https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION \
    && chmod +x /usr/local/bin/docker \
    && curl -fLo /usr/local/bin/docker-compose \
    https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-compose-`uname -s`-`uname -m` \
    && chmod +x /usr/local/bin/docker-compose

# Install node
ENV NVM_DIR /usr/local/nvm
ENV NVM_VERSION 0.27.1
ENV NODE_VERSION 4.1.1
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$PATH
RUN curl https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh | bash \
    && source $NVM_DIR/nvm.sh \
    && nvm install v$NODE_VERSION \
    && nvm use v$NODE_VERSION \
    && nvm alias default v$NODE_VERSION

# Install npm packages
RUN source $NVM_DIR/nvm.sh \
    && npm install -g \
    jshint

# Install gems
RUN gem install \
  tmuxinator

# Install go
ENV GO_VERSION 1.5.1
RUN curl -fL https://storage.googleapis.com/golang/go$GO_VERSION.linux-amd64.tar.gz \
    | tar -C /usr/local -xz

# Home sweet home
ENV HOME /home
WORKDIR $HOME

# Better zsh with prezto
COPY prezto $HOME/.zprezto
RUN chsh -s /bin/zsh \
  && for rc in $HOME/.zprezto/runcoms/z* ; do \
  ln -s "${rc}" "$HOME/.$(basename $rc)" ; done \
  && exec zsh && setopt EXTENDED_GLOB

# Add zsh completion
RUN curl -fLo $HOME/.zprezto/modules/completion/external/src/_tmuxinator \
  https://raw.githubusercontent.com/tmuxinator/tmuxinator/master/completion/tmuxinator.zsh \
  && curl -fLo $HOME/.zprezto/modules/completion/external/src/_docker \
  https://raw.githubusercontent.com/docker/docker/master/contrib/completion/zsh/_docker

# Dot it up
COPY dotfiles $HOME/.dotfiles
RUN for rc in $HOME/.dotfiles/* ; do \
  ln -s "${rc}" "$HOME/.$(basename $rc)" ; done

# Install vim plugins
RUN curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim \
    && mkdir -p ~/.vim/plugged \
    && vim +PlugInstall +qall

CMD ["zsh"]
