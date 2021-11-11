FROM artsy/ruby:2.6.5-node-chrome
ENV LANG C.UTF-8

ARG BUNDLE_GITHUB__COM

RUN apt-get update -qq && apt-get install -y \
  dumb-init \
  libpq-dev \
  postgresql-client \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set up deploy user, working directory and shared folders for Puma / Nginx
RUN adduser --disabled-password --gecos '' deploy && \
    mkdir -p /app && \
    chown deploy:deploy /app && \
    mkdir /shared && \
    mkdir /shared/config && \
    mkdir /shared/pids && \
    mkdir /shared/sockets && \
    chown -R deploy:deploy /shared

RUN gem install bundler:1.17.2

# Throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

# Set up gems
WORKDIR /tmp
ADD .ruby-version .ruby-version
ADD Gemfile Gemfile
ADD Gemfile.lock Gemfile.lock
RUN bundle install -j4

# Switch to deploy user
USER deploy
ENV USER deploy
ENV HOME /home/deploy

# Finally, add the rest of our app's code
# (this is done at the end so that changes to our app's code
# don't bust Docker's cache)
ADD --chown=deploy:deploy . /app
WORKDIR /app

RUN yarn install && yarn cache clean

# Precompile Rails assets
RUN bundle exec rake assets:precompile

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["bundle", "exec", "puma", "-C", "config/puma.config"]
