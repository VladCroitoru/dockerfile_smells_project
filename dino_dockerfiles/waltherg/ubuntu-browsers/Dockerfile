FROM ubuntu:16.04

MAINTAINER Georg Walther <contact@georg.io>

RUN apt-get update \
    && apt-get install -y --no-install-recommends wget \
    && wget --no-check-certificate https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome*.deb; exit 0

RUN apt-get -y --no-install-recommends -f install; exit 0

RUN apt-get -y --no-install-recommends install firefox

RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && apt-get update \
    && apt-get install -y --no-install-recommends bzip2 \
    && tar xf phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/
