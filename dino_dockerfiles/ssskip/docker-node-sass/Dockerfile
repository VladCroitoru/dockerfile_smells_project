FROM node:9.6.0-alpine

RUN apk add --no-cache \
        python \
        git \
        make \
        gcc \
        g++ \
        sudo \
        ruby \
        ruby-dev \
        openssl-dev \
        linux-headers

RUN npm install -g grunt-cli bower jsonlint-cli

RUN gem install compass --no-document