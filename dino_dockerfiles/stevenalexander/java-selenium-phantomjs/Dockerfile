FROM java:8-jdk

MAINTAINER Steven Alexander "steven.william.alexander@googlemail.com"

ENV PHANTOMJS_VERSION 2.0

# Install dependencies
RUN apt-get update && \
    apt-get install -y git-core build-essential g++ flex bison gperf ruby perl \
      libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
      libpng-dev libjpeg-dev python libx11-dev libxext-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install PhantomJS
RUN git clone https://github.com/ariya/phantomjs.git && \
    cd phantomjs && \
    git checkout ${PHANTOMJS_VERSION} && \
    ./build.sh --confirm && \
    cd / && \
    mv phantomjs/bin/phantomjs bin/. && \
    rm -rf phantomjs
