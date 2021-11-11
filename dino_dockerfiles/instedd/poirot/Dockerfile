FROM instedd/nginx-rails-20

# Install gem bundle
ADD Gemfile /app/
ADD Gemfile.lock /app/
ADD hercule.gemspec /app/
ADD lib/hercule/ /app/lib/hercule/
ADD lib/hercule.rb /app/lib/
RUN bundle install --jobs 3 --deployment --without development test

# Install the application
ADD . /app

# Precompile assets
RUN bundle exec rake assets:precompile RAILS_ENV=production SECRET_KEY_BASE=secret

# Add config files
ADD docker/runit-web-run /etc/service/web/run
ADD docker/database.yml /app/config/database.yml
