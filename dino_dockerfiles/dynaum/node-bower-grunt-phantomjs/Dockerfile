# Pull base image.
FROM dockerfile/nodejs-bower-grunt

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
  libfontconfig1-dev \
  libicu-dev \
  libfreetype6 \
  libpng-dev \
  libjpeg-dev 

# Phantomjs 1.9.7
RUN \
  cd /usr/local/share && \
  curl -L -O https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2 && \
  tar xjf phantomjs-1.9.7-linux-x86_64.tar.bz2 && \
  ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs && \
  ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs && \
  ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/bin/phantomjs

RUN \
  echo "export PHANTOMJS_BIN=/usr/bin/phantomjs" >> .bashrc

CMD "bash"
