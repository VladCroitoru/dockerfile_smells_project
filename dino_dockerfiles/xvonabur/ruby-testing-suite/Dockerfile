FROM ubuntu:14.04
MAINTAINER XvonabuR <webdev.xvonabur@gmail.com>
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  build-essential \
  cmake \
  curl \
  dbus \
  git-core \
  gstreamer1.0-plugins-base \
  gstreamer1.0-tools \
  gstreamer1.0-x \
  libcurl4-openssl-dev \
  libffi-dev \
  libgdbm-dev \
  libicu-dev \
  libncurses5-dev \
  libqt5webkit5-dev \
  libpq-dev \
  libreadline-dev \
  libssl-dev \
  libxml2-dev \
  libxslt-dev \
  libyaml-dev \
  logrotate \
  nodejs-legacy \
  nodejs \
  npm \
  pkg-config \
  python-docutils \
  qt5-default \
  software-properties-common \
  tar \
  wget \
  xvfb \
  zip \
  zlib1g-dev
RUN apt-add-repository ppa:brightbox/ruby-ng
RUN apt-get update
RUN apt-get install -y \
  ruby2.2 \
  ruby2.2-dev \
&& rm -rf /var/lib/apt/lists/*
RUN gem install bundler --no-ri --no-rdoc
RUN wget http://ftp.gnu.org/gnu/wget/wget-1.17.1.tar.gz
RUN tar -xzf wget-1.17.1.tar.gz
RUN cd wget-1.17.1 && ./configure --with-ssl=openssl && make && make install
RUN rm -rf wget-1.17.1 && rm wget-1.17.1.tar.gz
RUN npm install -g bower
RUN npm install -g phantomjs-prebuilt
RUN touch /root/.bowerrc && echo '{ "allow_root": true }' > /root/.bowerrc 
RUN touch /etc/machine-id && dbus-uuidgen > /etc/machine-id
