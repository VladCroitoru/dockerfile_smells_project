FROM buildpack-deps:xenial
MAINTAINER Fletcher91 <thom@argu.co>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get clean -qq && \
    apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-key adv --keyserver pgp.mit.edu --recv D101F7899D41F3C3
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install -y \
      bison build-essential curl g++ gcc git libc6-dev libgdbm3 \
      libgdbm-dev libgsf-1-dev libncurses5-dev libpq-dev libqt5webkit5-dev \
      libreadline6-dev libvips-dev make openjdk-7-jdk qt5-default yarn
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Docker
ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 1.11.2
ENV DOCKER_SHA256 8c2e0c35e3cda11706f54b2d46c2521a6e9026a7b13c7d4b8ae1f3a706fc55e1

RUN set -x \
	&& curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" -o docker.tgz \
	&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \
	&& tar -xzvf docker.tgz \
	&& mv docker/* /usr/local/bin/ \
	&& rmdir docker \
	&& rm docker.tgz \
	&& docker -v

# Install rbenv
ENV RBENV_DIR /root/.rbenv
ENV RBENV_VER v1.0.0
RUN git clone --depth 1 --branch $RBENV_VER -q https://github.com/rbenv/rbenv.git $RBENV_DIR
ENV PATH ${RBENV_DIR}/bin:${RBENV_DIR}/shims:${PATH}
RUN echo 'eval "$(rbenv init -)"' >> $HOME/.bashrc && \
      echo 'eval "$(rbenv init -)"' >> $HOME/.profile && \
      . $HOME/.profile
RUN git clone --depth 1 -q https://github.com/rbenv/ruby-build.git $RBENV_DIR/plugins/ruby-build


# Install nvm
ENV NVM_DIR /usr/local/.nvm
ENV NVM_VER v0.33.0
RUN git clone --depth 1 --branch $NVM_VER https://github.com/creationix/nvm.git $NVM_DIR && \
    cd $NVM_DIR && \
    git checkout `git describe --abbrev=0 --tags`
RUN echo ". ${NVM_DIR}/nvm.sh" > $HOME/.profile && \
    $NVM_DIR/install.sh && \
    . $HOME/.profile

# Install Go
ENV GOLANG_VERSION 1.7
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 702ad90f705365227e902b42d91dd1a40e48ca7f67a2f4b2fd052aaa4295cd95

RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
	&& echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
	&& tar -C /usr/local -xzf golang.tar.gz \
	&& rm golang.tar.gz

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"


# Install Ruby
ENV RUBY_VERSION 2.3.1
RUN $HOME/.rbenv/bin/rbenv install $RUBY_VERSION && \
    $HOME/.rbenv/bin/rbenv global $RUBY_VERSION
RUN gem install bundle bundler --no-rdoc --no-ri

# Install Node
ENV NODE_VERSION 6.9.5
RUN . $NVM_DIR/nvm.sh && \
    nvm install $NODE_VERSION && \
    nvm alias default $NODE_VERSION && \
    nvm use default
ENV NODE_PATH ${NVM_DIR}/v${NODE_VERSION}/lib/node_modules
ENV PATH ${NVM_DIR}/versions/node/v${NODE_VERSION}/bin:${PATH}

RUN mkdir -p /go/src/app
WORKDIR /go/src/app
