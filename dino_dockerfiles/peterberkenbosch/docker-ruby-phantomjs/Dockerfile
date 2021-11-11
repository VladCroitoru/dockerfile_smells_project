FROM ruby:2.2.3

ENV PHANTOM_JS="phantomjs-1.9.8-linux-x86_64"

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential chrpath libssl-dev libxft-dev libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev && \
    curl -L -O https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 && \
    tar xvjf $PHANTOM_JS.tar.bz2 && \
    mv $PHANTOM_JS /usr/local/share && \
    ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
