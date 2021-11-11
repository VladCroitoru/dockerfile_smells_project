FROM ruby:2.3.1
MAINTAINER prime8@users.noreply.github.com

ENV PHANTOMJSVER=2.1.1

RUN curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJSVER-linux-x86_64.tar.bz2 \
   | tar -C /usr/local --no-same-owner -jx \
  && ln -s /usr/local/phantomjs-$PHANTOMJSVER-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs \
  && which phantomjs \
  && echo "PhantomJS version $(phantomjs --version) installed"
