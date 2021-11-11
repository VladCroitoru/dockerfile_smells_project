FROM alpine:3.3
MAINTAINER Björn Dahlgren <bjorn@dahlgren.at>

# Packages required to generate tiles
ENV PACKAGES build-base imagemagick-dev ruby ruby-bundler ruby-dev ruby-io-console

# Install build dependencies
RUN apk update && \
  apk upgrade && \
  apk add --virtual build-dependencies $PACKAGES && \
  rm -rf /var/cache/apk/*

# Setup work directory
ENV APP_HOME /worlds
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install required gems for building the app
COPY Gemfile $APP_HOME
COPY Gemfile.lock $APP_HOME
RUN bundle install

# Copy required workspace files to image
COPY generate_tiles.rb $APP_HOME
COPY worlds $APP_HOME/worlds

# Generate tiles
RUN ruby generate_tiles.rb

# Remove unwanted files
RUN gem uninstall --all -x -I
RUN rm Gemfile*
RUN rm generate_tiles.rb
RUN rm -r worlds

# Remove build dependencies
RUN apk del build-dependencies

# Declare work directory as volume
VOLUME $APP_HOME
