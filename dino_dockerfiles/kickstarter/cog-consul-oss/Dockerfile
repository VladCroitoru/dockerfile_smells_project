FROM alpine:3.4

RUN apk -U add ca-certificates ruby ruby-bundler ruby-dev ruby-io-console ruby-irb ruby-rdoc ruby-json bash

# Setup bundle user and directory
RUN adduser -h /home/bundle -D bundle && \
    mkdir -p /home/bundle && \
    chown -R bundle /home/bundle

# Copy the bundle source to the image
WORKDIR /home/bundle
COPY Gemfile Gemfile.lock /home/bundle/

# Install Git, run Bundler, and uninstall Git to recover space
RUN apk add git && \
    su bundle -c 'bundle install --without development --path .bundle' && \
    apk del git && \
    rm -f /var/cache/apk/*

# Copy rest of code
COPY . /home/bundle

# Drop privileges
USER bundle
