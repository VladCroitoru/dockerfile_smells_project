FROM ruby:latest

MAINTAINER Allister Antosik <me@allisterantosik.com>

# Install dependencies

# Set an environment variable to store where the app is installed to inside
# of the Docker image.
ENV INSTALL_PATH /juno-probe
RUN mkdir -p $INSTALL_PATH

# This sets the context of where commands will be ran in and is documented
# on Docker's website extensively.
WORKDIR $INSTALL_PATH

# Ensure gems are cached and only get updated when they change. This will
# drastically increase build times when your gems do not change.
COPY Gemfile Gemfile
RUN bundle install

# Copy in the application code from your work station at the current directory
# over to the working directory.
COPY . .

CMD bundle exec ruby app.rb
