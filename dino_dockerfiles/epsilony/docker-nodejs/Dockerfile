# use nodejs in China mainland, according to the silly network environment

FROM epsilony/baseimage

MAINTAINER Man YUAN

RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -
RUN apt-get -y install nodejs
RUN npm install  -g cnpm --registry=https://registry.npm.taobao.org && \
  cnpm install -g bower \
  requirejs \
  grunt-cli \
  coffee-script \
  karma \
  nodemon \
  gulp \
  browserify \
  jspm \
  browser-sync

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
