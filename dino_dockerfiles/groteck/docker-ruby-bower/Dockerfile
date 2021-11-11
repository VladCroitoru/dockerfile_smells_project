FROM ruby:2.1.2

MAINTAINER Juan Fraire

RUN cd \
    &&  git clone https://github.com/joyent/node.git \
    &&  cd node \
    &&  git checkout v0.10.33 \
    &&  ./configure \
    &&  make \
    &&  make install \
    &&  cd .. \
    &&  rm -rfv ~/node

RUN npm install -g bower
