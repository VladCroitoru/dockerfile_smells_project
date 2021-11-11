FROM node:6

MAINTAINER Richard <hello@noxan.net>

ENV PHANTOM_VERSION="2.1.1"

RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOM_VERSION-linux-x86_64.tar.bz2

RUN tar xvf phantomjs-$PHANTOM_VERSION-linux-x86_64.tar.bz2

RUN mv phantomjs-2.1.1-linux-x86_64 /usr/local/share/
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/
