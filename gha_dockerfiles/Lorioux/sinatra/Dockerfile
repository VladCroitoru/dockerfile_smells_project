# Base ruby image to build the .gem files:
FROM ruby:3.0.2-slim AS builder
# Update the image and install dependencies
RUN apt-get update --no-install-recommends \
    && apt-get install -y build-essential --no-install-recommends

# Prepare a working directory
RUN mkdir -p build
WORKDIR /build 

# Update the bundler
RUN gem install bundler
# Copy dependecies files
COPY Gemfile .
COPY Gemfile.lock .

# Install .gem dependencies
RUN bundle install 

# Remove dependencies
RUN apt-get autoremove -y build-essential


# Production ruby image
FROM ruby:3.0.2-alpine AS base
ARG VERSION
WORKDIR /home
COPY --from=builder /usr/local/bundle/ /usr/local/bundle/
RUN bundle config set --local BUNDLE_PATH '/usr/local/bundle' \
    && export "GEM_PATH=/usr/local/bundle" >> .bashrc
# copy remaining content into the working directory
# COPY --from=builder /build config ./
# COPY --from=builder /build config.ru ./
# COPY --from=builder /build lib ./
# copy remaining content into the working directory
COPY config .
COPY config.ru .
COPY lib .



# ENV RACK_ENV "production"
ENV PORT 80
ENV WEB_CONCURRENCY 4
ENV MAX_THREADS 1000

ENV VERSION "1.0.0"

LABEL version=$VERSION project="Sinatra"


EXPOSE $PORT

CMD [ "puma", "-C", "config/puma.rb" ]
