FROM instedd/nginx-rails:1.9

# Install gem bundle
ADD Gemfile /app/
ADD Gemfile.lock /app/
RUN bundle install --jobs 3 --deployment --without development test

# Install the application
ADD . /app

# Generate version file
RUN if [ -d .git ]; then git describe --always > VERSION; fi

# Precompile assets
RUN bundle exec rake assets:precompile RAILS_ENV=production

# Add config files
ADD docker/runit-web-run /etc/service/web/run
ADD docker/database.yml /app/config/database.yml
ADD docker/amqp.yml /app/config/amqp.yml
ADD docker/migrate /app/migrate
