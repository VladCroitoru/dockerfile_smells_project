FROM microsoft/dotnet

RUN apt-get -qq update \
    && apt-get -qqy install \
    bzip2 \
    libfontconfig1 \
    \
    && cd /root \
    && wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && tar xvf phantomjs-2.1.1-linux-x86_64.tar.bz2 \
    && cp /root/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin
