# TODO: use https://gist.github.com/Xotabu4/a243d9ff25cfe276bcaa0175fb6a4b00
FROM alpine:3.7

RUN apk add --no-cache \
    nodejs unzip curl \
    python \
    build-base \
    git \
    bash \
    openjdk8-jre-base \
    # chromium dependencies
    udev \
    ttf-freefont \
    chromium-chromedriver \
    chromium && \
    rm -rf /var/cache/apk/*

# https://raw.githubusercontent.com/blairg/docker-node-sass-alpine/master/Dockerfile
# install libsass
RUN git clone https://github.com/sass/sassc && cd sassc && \
    git clone https://github.com/sass/libsass && \
    SASS_LIBSASS_PATH=/sassc/libsass make && \
    mv bin/sassc /usr/bin/sassc && \
    cd ../ && rm -rf /sassc

# created node-sass binary
ENV SASS_BINARY_PATH=/usr/lib/node_modules/node-sass/build/Release/binding.node
RUN git clone --recursive https://github.com/sass/node-sass.git && \
    cd node-sass && \
    git submodule update --init --recursive && \
    npm install && \
    node scripts/build -f && \
    cd ../ && rm -rf node-sass

# add binary path of node-sass to .npmrc
RUN touch $HOME/.npmrc && echo "sass_binary_cache=${SASS_BINARY_PATH}" >> $HOME/.npmrc

ENV SKIP_SASS_BINARY_DOWNLOAD_FOR_CI true
ENV SKIP_NODE_SASS_TESTS true