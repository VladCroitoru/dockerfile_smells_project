FROM node

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        gperf bison ruby flex \
        # perl python \
        libicu52 libfontconfig1 libjpeg62 libpng12-0 \
        libfontconfig1-dev libicu-dev libfreetype6 libx11-dev libxext-dev \
    && cd /tmp \
    && git clone git://github.com/ariya/phantomjs.git \
    && cd /tmp/phantomjs \
    && git checkout 2.0 \
    && ./build.sh --confirm \
    && mv /tmp/phantomjs/bin/phantomjs /usr/bin/phantomjs \
    && chmod +x /usr/bin/phantomjs \
    && rm -rf /tmp/phantomjs \
    && apt-get remove -y \
        build-essential gperf bison ruby flex perl python \
        libfontconfig1-dev libicu-dev libfreetype6 libx11-dev libxext-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/

RUN npm install -g phantom \
    && rm -rf /tmp/npm-*