# Pull base image.
FROM ubuntu:14.04

VOLUME ["/azk/npm"]

# Ignore APT warnings about not having a TTY
ENV DEBIAN_FRONTEND noninteractive

# dependencies
RUN \
  apt-get update && \
  apt-get -y install \
  build-essential \
  curl \
  git-core \
  python-software-properties \
  libcurl4-openssl-dev \
  libc6-dev \
  libreadline-dev \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  libyaml-dev \
  zlib1g-dev \
  vim \
  g++ \
  flex \
  bison \
  gperf \
  perl \
  libsqlite3-dev \
  libfontconfig1-dev \
  libicu-dev \
  libfreetype6 \
  libssl-dev \
  libpng-dev \
  libjpeg-dev

# Ruby install
RUN \
  curl --progress http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz | tar xz && \
  cd ruby-2.1.2 && \
  ./configure --disable-install-doc && \
  make && make install && \
  cd .. && rm -rf ruby-2.1.2* && \
  echo 'gem: --no-document' > /usr/local/etc/gemrc && \
  gem install bundler

# Install Node.js
RUN \
  apt-get install -y nodejs-legacy npm && \
  npm install -g grunt-cli && \
  npm install -g bower

# Phantomjs 1.9.7
RUN \
  cd /usr/local/share && \
  curl -L -O https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2 && \
  tar xjf phantomjs-1.9.7-linux-x86_64.tar.bz2 && \
  ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs && \
  ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs && \
  ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/bin/phantomjs

# Adding bin folders on PATH
RUN \
  echo "export PATH=$HOME/bin:/azk/npm/bin:$PATH" > .bashrc

CMD "bash"
