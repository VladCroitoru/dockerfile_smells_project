# This file was created by referencing:
# https://docs.docker.com/geot-started/part2/#sample-dockerfile
# https://hub.docker.com/_/Ruby

# Use the official image as a parent image.
FROM ruby:2.7

# Throw errors if Gemfile has been modified since Gemfile.lock.
RUN bundle config --global frozen 1

# Set the working directory.
WORKDIR /usr/src/app

# Copy the file from your host to your current location.
COPY Gemfile Gemfile.lock ./

# Run the command inside your image filesystem.
RUN bundle install

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 4000 35729

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Run the specified command within the container.
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--drafts", "--livereload"]