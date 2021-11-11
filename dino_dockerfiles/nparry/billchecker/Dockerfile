FROM ubuntu:16.10

RUN apt-get update && apt-get upgrade -y

RUN apt-get -y install libssl-dev
RUN apt-get -y install ruby
RUN apt-get -y install ruby-dev
RUN apt-get -y install build-essential
RUN apt-get -y install libxslt-dev
RUN apt-get -y install libxml2-dev
RUN apt-get -y install zlib1g-dev
RUN apt-get -y install fontconfig

# Speed up Docker images rebuilding during dev
RUN gem install capybara --no-rdoc --no-ri
RUN gem install poltergeist --no-rdoc --no-ri
RUN gem install redis --no-rdoc --no-ri
RUN gem install encryptor --no-rdoc --no-ri
RUN gem install slack-ruby-bot --no-rdoc --no-ri
RUN gem install bundler --no-rdoc --no-ri
RUN gem install pry --no-rdoc --no-ri

ADD https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 /tmp/
RUN cd /tmp && bzcat phantomjs* | tar x && mv phantomjs*/bin/* /usr/local/bin && rm -rf phantomjs*

RUN mkdir -p /tmp/billchecker_gem
COPY . /tmp/billchecker_gem/
RUN cd /tmp/billchecker_gem && gem build billchecker.gemspec && gem install billchecker*.gem --no-rdoc --no-ri
RUN cd / && rm -rf /tmp/billchecker_gem

RUN adduser --system --shell /bin/bash billchecker
USER billchecker

