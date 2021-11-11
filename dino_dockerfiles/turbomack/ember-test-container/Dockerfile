FROM ubuntu:14.04
MAINTAINER turbomack

# Dependencies we just need for building phantomjs
ENV buildDependencies \
    wget \
    unzip \
    python \
    g++ \
    flex \
    bison \
    gperf \
    ruby \
    perl \
    libsqlite3-dev \
    libpng-dev \
    git-core \
    curl \
    zlib1g-dev \
    build-essential \
    libssl-dev \
    libreadline-dev \
    libyaml-dev

# Dependencies we need for running phantomjs
ENV phantomJSDependencies \
    libicu-dev \
    libfontconfig1-dev \
    libjpeg-dev \
    libfreetype6

# Installing phantomjs
RUN \
    # Installing dependencies
    apt-get update -yqq \
&&  apt-get install -fyqq ${buildDependencies} ${phantomJSDependencies} \
    # Downloading src, unzipping & removing zip
&&  mkdir phantomjs \
&&  cd phantomjs \
&&  wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.0.0-source.zip \
&&  unzip phantomjs-2.0.0-source.zip \
&&  rm -rf /phantomjs/phantomjs-2.0.0-source.zip \
    # Building phantom
&&  cd phantomjs-2.0.0/ \
&&  ./build.sh --confirm --silent \
    # Removing everything but the binary
&&  ls -A | grep -v bin | xargs rm -rf \
    # Symlink phantom so that we are able to run `phantomjs`
&&  ln -s /phantomjs/phantomjs-2.0.0/bin/phantomjs /usr/local/share/phantomjs \
&&  ln -s /phantomjs/phantomjs-2.0.0/bin/phantomjs /usr/local/bin/phantomjs \
&&  ln -s /phantomjs/phantomjs-2.0.0/bin/phantomjs /usr/bin/phantomjs \
    # Checking if phantom works
&&  phantomjs -v


# Install NODE.js v 0.12.x
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -
RUN apt-get install -yq nodejs

# Install bower
RUN npm install -g bower

# Removing build dependencies, clean temporary files
RUN \
    apt-get purge -yqq  \
    wget \
    libreadline-dev \
    libyaml-dev \
    unzip \
    python \
    g++ \
    flex \
    bison \
    gperf \
    ruby \
    libsqlite3-dev \
    libpng-dev \
    build-essential \
    libssl-dev \
    libreadline-dev \
    libyaml-dev \
&&  apt-get autoremove -yqq \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install ruby
RUN \
    apt-get update \
&&  apt-get install -fyqq software-properties-common \
&&  apt-add-repository ppa:brightbox/ruby-ng \
&&  apt-get update \
&&  apt-get install -fyqq ruby2.2

# test after clean
RUN \
    phantomjs -v \
&&  node -v \
&&  npm -v \
&&  bower -v \
&&  ruby -v

