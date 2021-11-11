FROM ruby:alpine

RUN apk add --no-cache build-base libxml2-dev libxslt-dev \
    && gem install nokogiri

RUN apk add --no-cache openssl \
    && wget -O /tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2 https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && md5sum /tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
        | grep -q "1c947d57fce2f21ce0b43fe2ed7cd361" \
    && tar -xjf /tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /tmp \
    && rm -rf /tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && mv /tmp/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs \
    && rm -rf /tmp/phantomjs-2.1.1-linux-x86_64
