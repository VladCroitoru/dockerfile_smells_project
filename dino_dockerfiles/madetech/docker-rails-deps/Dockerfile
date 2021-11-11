FROM ubuntu:14.04.5

RUN apt-get update -qq
RUN apt-get -y install build-essential git openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev libmysqlclient-dev libpq-dev imagemagick libmagickwand-dev libffi-dev nodejs npm nodejs-legacy mysql-client libav-tools
RUN npm install -g phantomjs

RUN git clone https://github.com/sstephenson/ruby-build.git /tmp/ruby-build && \
  cd /tmp/ruby-build && \
  ./install.sh && \
  cd / && \
  rm -rf /tmp/ruby-build

RUN ruby-build -v 2.5.0 /usr/local
RUN gem install bundler rubygems-bundler --no-rdoc --no-ri
RUN gem regenerate_binstubs
