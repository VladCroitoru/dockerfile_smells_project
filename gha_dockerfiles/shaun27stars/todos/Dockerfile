# Use the Ruby 3.0.1 image from Docker Hub
# as the base image (https://hub.docker.com/_/ruby)
FROM ruby:2.7.4-slim-bullseye

# Use a directory called /code in which to store
# this application's files. (The directory name
# is arbitrary and could have been anything.)
ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y \
  curl \
  wget \
  build-essential \
  libpq-dev &&\
  curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
  apt-get update && apt-get install -y nodejs yarn

# # Install Yarn.
# RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
# RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
# RUN apt-get update && apt-get install -y yarn

# RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
# 	echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google.list && \
#   apt-get update && apt-get install -y google-chrome-stable


ENV LANG=C.UTF-8 \
  BUNDLE_JOBS=4 \
  BUNDLE_RETRY=3

# ADD Gemfile* $APP_HOME/

# # Run bundle install to install the Ruby dependencies.
# RUN bundle install

# ADD package.json yarn.lock $APP_HOME/
# # Run yarn install to install JavaScript dependencies.
# RUN yarn install --check-files

# Copy all the application's files into the /code
# directory.
ADD . $APP_HOME
EXPOSE 3000
# ENTRYPOINT ["bundle", "exec"]
# Set "rails server -b 0.0.0.0" as the command to
# run when this container starts.
# CMD ["rails", "server", "-b", "0.0.0.0"]