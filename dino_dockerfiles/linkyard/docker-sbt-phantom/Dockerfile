FROM linkyard/docker-sbt:13.15-8u121

RUN apt-get update && \
    apt-get install -y build-essential chrpath libssl-dev libxft-dev && \
    apt-get install -y libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev && \
    rm -rf /var/lib/apt/lists/*

ENV PHANTOM_JS_VERSION 2.1.1
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOM_JS_VERSION}-linux-x86_64.tar.bz2 -O /usr/local/share/phantomjs.tar.bz2 && \
    cd /usr/local/share && \
    tar xjf phantomjs.tar.bz2 && \
    rm phantomjs.tar.bz2 && \
    mv phantomjs-${PHANTOM_JS_VERSION}-linux-x86_64 phantomjs && \
    ln -sf /usr/local/share/phantomjs/bin/phantomjs /usr/local/bin

#Run sbt once to initialize it along with commonly used dependencies
# = We trade a bigger image size against faster builds
COPY init_deps /tmp/init
RUN cd /tmp/init && \
    sbt test && \
    rm -rf /tmp/init
