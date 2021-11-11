FROM ruby
MAINTAINER Matthew Sullivan <matthew@msull92.com>

# Install gems
ENV APP_HOME /app
ENV HOME /root
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
COPY Gemfile* $APP_HOME/
RUN bundle install

# Upload source
COPY . $APP_HOME

# Start script
CMD ["bundle", "exec", "ruby", "main.rb"]
