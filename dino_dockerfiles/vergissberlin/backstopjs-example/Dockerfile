FROM node

RUN  apt-get update &&\
 apt-get install -y mc vim tar wget build-essential chrpath \
  libssl-dev libxft-dev libfreetype6 libfreetype6-dev

RUN cd ~  &&\
  export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" &&\
  wget --max-redirect 100 https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 &&\
  tar xvjf $PHANTOM_JS.tar.bz2  -C /usr/local/share/ &&\
  ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

RUN npm cache clean -f &&\
 npm install -g n &&\
 n stable

RUN npm update &&\
 npm install -g backstopjs phantomjs slimerjs

WORKDIR backstopjs-example
