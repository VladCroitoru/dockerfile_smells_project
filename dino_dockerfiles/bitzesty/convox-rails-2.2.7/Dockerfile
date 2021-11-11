FROM ubuntu:16.04

RUN apt-get update && apt-get -y install \
  build-essential \
  git \
  wget \
  libcurl4-openssl-dev \
  liblzma-dev \
  libmysqld-dev \
  libpq-dev \
  libsqlite3-dev \
  nodejs \
  rbenv \
  ruby-build \
  ruby-dev \
  tzdata \
  zlib1g-dev \
  libfreetype6 \ 
  libfreetype6-dev \
  libfontconfig1 \
  libfontconfig1-dev \
  openssl \
  libssl-dev \
  libxrender-dev \
  libxrender1 \
  libxtst6 \
  libxi6 \  
  imagemagick \ 
  libmagickwand-dev

RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections
RUN apt-get update && apt-get install -y ttf-mscorefonts-installer apt-transport-https

ENV SSL_CERT_DIR=/etc/ssl/certs
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

ARG RUBY_VERSION=2.2.7
ENV PATH /root/.rbenv/shims:${PATH}
RUN git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build \
  && rbenv install ${RUBY_VERSION} \
  && rbenv global ${RUBY_VERSION}

ARG BUNDLER_VERSION=1.16.0
RUN gem install bundler -v ${BUNDLER_VERSION} && rbenv rehash

ARG NODE_VERSION=7.7.1
ENV NVM_DIR=/root/.nvm
ENV PATH /root/.nvm/versions/node/v${NODE_VERSION}/bin:${PATH}
RUN curl -s https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash \
  && . /root/.nvm/nvm.sh \
  && nvm install ${NODE_VERSION} \
  && nvm alias default ${NODE_VERSION} \
  && nvm use default

RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
  && tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/ \
  && ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin


WORKDIR /app

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
