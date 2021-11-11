FROM instedd/nginx-rails:2.2

# Install gem bundle
ADD Gemfile /app/
ADD Gemfile.lock /app/
RUN bundle install --jobs 3 --deployment --without development test

# Default environment settings
ENV PUMA_OPTIONS "--preload -w 4"

# Install the application
ADD . /app

# Precompile assets
RUN bundle exec rake assets:precompile RAILS_ENV=production SECRET_KEY_BASE=secret

# Add config files
ADD docker/runit-web-run /etc/service/web/run
ADD docker/migrate /app/migrate

# Runs web on port 80
EXPOSE 80
