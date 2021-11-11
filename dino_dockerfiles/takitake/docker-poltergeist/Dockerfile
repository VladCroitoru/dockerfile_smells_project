FROM ruby:2.2.4

# http://phantomjs.org/build.html
# https://github.com/sparklemotion/nokogiri.org-tutorials/blob/master/content/installing_nokogiri.md
RUN apt-get update \
  && apt-get install -y git curl build-essential g++ flex bison gperf perl \
     libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
     libpng-dev libjpeg-dev python libx11-dev libxext-dev zlib1g-dev libreadline-dev \
  && apt-get clean

# Install PhantomJS
RUN git clone --recurse-submodules https://github.com/ariya/phantomjs.git /usr/local/phantomjs \
  && cd /usr/local/phantomjs \
  && ./build.py \
  && ln -s /usr/local/phantomjs/bin/phantomjs /usr/local/bin/phantomjs

# Cache poltergeist gem
RUN gem install poltergeist -v 1.8.1
