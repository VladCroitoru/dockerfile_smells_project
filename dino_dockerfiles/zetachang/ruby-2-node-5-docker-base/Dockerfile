FROM debian:jessie

# Install dependencies
RUN apt-get update && apt-get install -y curl \
  autoconf \
  bison \
  build-essential \
  libssl-dev \
  libyaml-dev \
  libreadline6-dev \
  zlib1g-dev \
  libncurses5-dev

# Install ruby-build
RUN curl -L https://github.com/rbenv/ruby-build/archive/v20160426.tar.gz -o ruby-build.tar.gz &&\
  tar -xzf ruby-build.tar.gz &&\
  rm ruby-build.tar.gz &&\
  ruby-build-20160426/install.sh &&\
  rm -rf ruby-build-20160426

# Install Ruby 2.1.10 and Bundler
RUN /usr/local/bin/ruby-build 2.1.10 /opt/ruby-2.1.10
RUN /opt/ruby-2.1.10/bin/gem install bundler

# set up path for all users
ENV PATH /opt/ruby-2.1.10/bin:$PATH
RUN echo "PATH=/opt/ruby-2.1.10/bin:$PATH" >> /etc/profile

# Install all required utility package
RUN apt-get update -qq && \
apt-get install -y libpq-dev postgresql-client \
libmagickwand-dev imagemagick

# Install NodeJS 5
# according to https://github.com/nodesource/distributions#installation-instructions
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
apt-get install -y nodejs

# Install ffmpeg
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list && \
     echo "deb-src http://www.deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list && \
     apt-get update && \
     apt-get -y --force-yes install deb-multimedia-keyring && \
     apt-get update && \
     apt-get -y install ffmpeg
     
# Install git (in case some gem is not published on rubygems.org)
RUN apt-get update && apt-get install -y git

