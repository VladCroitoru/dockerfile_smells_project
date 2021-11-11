FROM ruby:2.3.3-alpine

RUN apk -U add ca-certificates && \
    rm -f /var/cache/apk/*

# Setup bundle user and directory
RUN adduser -h /home/bundle -D bundle && \
    mkdir -p /home/bundle && \
    chown -R bundle /home/bundle

# Copy the bundle source to the image
WORKDIR /home/bundle
COPY Gemfile Gemfile.lock /home/bundle/

# Install Git and packages to build libgit2, run Bundler, and uninstall
# packages recover space
RUN su bundle -c 'bundle install --standalone --without="development test"'

# Copy rest of code
COPY . /home/bundle

# Drop privileges
USER bundle
