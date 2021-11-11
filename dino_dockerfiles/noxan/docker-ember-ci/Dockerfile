FROM node:6

MAINTAINER Richard <hello@noxan.net>

ENV PHANTOM_VERSION="2.1.1"

RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOM_VERSION-linux-x86_64.tar.bz2

RUN tar xvf phantomjs-$PHANTOM_VERSION-linux-x86_64.tar.bz2

RUN mv phantomjs-$PHANTOM_VERSION-linux-x86_64 /usr/local/share/
RUN ln -sf /usr/local/share/phantomjs-$PHANTOM_VERSION-linux-x86_64/bin/phantomjs /usr/local/bin/

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update
RUN apt-get install yarn

# Install ember-cli and bower
RUN yarn global add ember-cli bower
