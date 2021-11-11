FROM ruby:2.4.0

# Install prerequisites
RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install gem bundle
ADD Gemfile /app/
ADD Gemfile.lock /app/
WORKDIR /app
RUN bundle install --jobs 3 --deployment --without development test

# Default environment settings
ENV PUMA_OPTIONS "--preload -w 4"
ENV RAILS_SERVE_STATIC_FILES "true"
ENV RAILS_ENV "production"
ENV SECRET_KEY_BASE "changeme"
ENV PORT "80"

# Install the application
ADD . /app

# Generate version file if needed
RUN if [ -d .git ]; then git describe --always > VERSION; fi

# Precompile assets
RUN bundle exec rake assets:precompile RAILS_ENV=production SECRET_KEY_BASE=secret

# Run server on command
EXPOSE $PORT
CMD bundle exec rails server -e production -p $PORT
