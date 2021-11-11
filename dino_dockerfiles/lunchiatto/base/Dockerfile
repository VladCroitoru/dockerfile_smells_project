FROM ruby:2.4.1-slim

# deps
RUN apt-get update -qq && \
    apt-get install -y build-essential git vim libpq-dev \
                       bash-completion curl
# node source
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install nodejs

# Environment variables
ENV APP_HOME=/usr/src/app
RUN gem install bundler -v 1.15.3
ENV BUNDLE_WITHOUT=development:test
ENV BUNDLE_FROZEN=true
RUN bundle config --global jobs 8

# setup the directory
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
