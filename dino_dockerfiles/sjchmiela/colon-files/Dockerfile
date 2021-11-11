FROM ruby:2.2.3

## Add app code and install dependencies
RUN gem install bundler
ADD app/Gemfile /opt/app/Gemfile
RUN cd /opt/app; bundle install
COPY app/ /opt/app

EXPOSE 80

## Startup command
CMD BUNDLE_GEMFILE=/opt/app/Gemfile bundle exec ruby /opt/app/app.rb
