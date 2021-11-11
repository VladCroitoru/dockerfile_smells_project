FROM parafuzo/ruby-base
MAINTAINER dev@parafuzo.com

RUN apk add --update nodejs curl python && \
    npm install -g yarn

# Phantomjs 1.9.7
RUN \
  cd /usr/local/share && \
  curl -L -O https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2 && \
  tar xjf phantomjs-1.9.7-linux-x86_64.tar.bz2 && \
  ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs && \
  ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs && \
  ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/bin/phantomjs

CMD ["/bin/sh"]
