FROM ruby:2.2.3

# Get linux ready
RUN apt-get update -qq && apt-get install -y build-essential  mysql-client libmysqlclient-dev

# for a JS runtime
RUN apt-get install -y nodejs

# Creates the app home directory
ENV APP_HOME /people
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile* $APP_HOME/
RUN gem install bundler
RUN bundle install

ADD . $APP_HOME

# Define the script we want run once the container boots
# Use the "exec" form of CMD so our script shuts down gracefully on SIGTERM (i.e. `docker stop`)
CMD [ "foreman", "start"]