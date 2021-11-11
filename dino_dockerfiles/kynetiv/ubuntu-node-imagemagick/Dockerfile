FROM ubuntu:xenial-20170915

MAINTAINER Miles Fink

RUN apt-get update && apt-get install -y git curl imagemagick

ENV NVM_DIR /usr/local/nvm
ENV NODE_DEFAULT_VERSION 7.10.1
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.4/install.sh | bash \
  && . "$NVM_DIR/nvm.sh" \
  && nvm install $NODE_DEFAULT_VERSION \
  && nvm use $NODE_DEFAULT_VERSION \
  && echo 'export OLD_PREFIX=$PREFIX && unset PREFIX' > $HOME/.profile \
  && echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"' >> $HOME/.profile \
  && echo 'export PREFIX=$OLD_PREFIX && unset OLD_PREFIX' >> $HOME/.profile \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

