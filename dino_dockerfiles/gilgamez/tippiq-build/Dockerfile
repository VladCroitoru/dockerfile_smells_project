FROM node:4
MAINTAINER Gilgamesh Nootebos <gilgamez@gmail.com>
RUN \
  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
  apt-get update && \
  apt-get install --no-install-recommends -y bundler ruby-dev google-chrome-stable && \
  gem install activesupport -v 4.2.5 && \
  gem install sass scss_lint mailcatcher && \
  npm install -g bower gulp knex mocha istanbul protractor && \
  webdriver-manager update && \
  rm -rf /var/lib/apt/lists/*
