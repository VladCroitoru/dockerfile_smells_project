FROM ruby:2.5

RUN apt-get update -y 
RUN apt-get install -y sudo bash
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo bash
RUN apt-get install -y nodejs
RUN apt-get clean

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
    && mkdir /tmp/phantomjs \
    && curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
           | tar -xj --strip-components=1 -C /tmp/phantomjs \
    && cd /tmp/phantomjs \
    && mv bin/phantomjs /usr/local/bin \
    && cd \
    && apt-get purge --auto-remove -y \
        curl \
    && apt-get clean \
    && rm -rf /tmp/* /var/lib/apt/lists/*

RUN gem install wraith --no-rdoc --no-ri
RUN gem install aws-sdk --no-rdoc --no-ri

# Make sure a recent (>6.7.7-10) version of ImageMagick is installed.
RUN apt-get install -y imagemagick

ENTRYPOINT [ "wraith" ]
