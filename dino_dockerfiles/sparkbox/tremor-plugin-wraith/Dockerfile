FROM ruby:2.3.1

# Install Node & phantomjs
RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_4.x | /bin/bash -
RUN apt-get install -y nodejs
RUN npm install -g phantomjs-prebuilt

ENV APP_HOME /wraith

# Create app dir and move to $APP
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install Gems
COPY Gemfile* $APP_HOME/
RUN bundle install
RUN gem install bundler

# Add the App
COPY . $APP_HOME

# This is necessary so that the image can be run as if a process
ENTRYPOINT ["ruby", "wraith-cli.rb", "check"]
