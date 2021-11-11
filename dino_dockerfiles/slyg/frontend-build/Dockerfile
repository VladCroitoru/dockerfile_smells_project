FROM node:6.3.0

# Ruby stuff
RUN apt-get update \
 && apt-get install -y \
    ruby \
    ruby-dev \
 && gem update --system \
 && gem install bundler
