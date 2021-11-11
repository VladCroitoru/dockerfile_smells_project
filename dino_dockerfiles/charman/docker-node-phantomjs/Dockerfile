# PhantomJS installation instructions adapted from:
#  https://hub.docker.com/r/wernight/phantomjs/~/dockerfile/
# but using 'node:latest' as the base image.

FROM node:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential g++ flex bison gperf ruby perl \
    libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
    libpng-dev libjpeg-dev python libx11-dev libxext-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvf phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
