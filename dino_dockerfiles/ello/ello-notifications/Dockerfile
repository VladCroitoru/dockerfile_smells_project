FROM ruby:2.6.7

# Run updates
RUN apt-get update -qq && apt-get install -y build-essential \
  libpq-dev

# Set up working directory
RUN mkdir /app
WORKDIR /app

# Set up gems
COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock
RUN BUNDLE_JOBS=7 bundle install

# Install foreman
RUN gem install foreman

# Add the rest of the app's code
COPY . /app
