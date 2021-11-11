FROM ubuntu:trusty

RUN apt-get update

RUN apt-get install -y build-essential
RUN apt-get install -y chrpath
RUN apt-get install -y libssl-dev
RUN apt-get install -y libxft-dev
RUN apt-get install -y libfreetype6
RUN apt-get install -y libfreetype6-dev
RUN apt-get install -y libfontconfig1
RUN apt-get install -y libfontconfig1-dev

ADD https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2 /tmp/phantomjs.tar.bz2

RUN mkdir /opt/phantomjs
RUN tar xf /tmp/phantomjs.tar.bz2 -C /opt/phantomjs --strip-components=1

ADD app /opt/app
