# Using official Ruby runtime base image
FROM ruby:2.3.1-slim

MAINTAINER "Toshiki Inami <t-inami@arukas.io>"

# Install curl, git and the other libraries
RUN apt-get update && apt-get install -y \
      git \
      libyaml-dev \
      libssl-dev \
      libreadline-dev \
      libxml2-dev \
      libxslt1-dev \
      libffi-dev \
      build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the applilcation directory
ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install gems
COPY Gemfile $APP_HOME/
RUN bundle install --jobs=4

# Copy our code from the current folder to /app inside the container
COPY . $APP_HOME

# Make port 4657 available for publish
EXPOSE 4567

# Start server
CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "4567"]
