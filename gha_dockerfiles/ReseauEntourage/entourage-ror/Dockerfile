##################################################################################
# This is a multi stage dockerfile
# https://docs.docker.com/develop/develop-images/multistage-build/
#
# The first main stage is prod. If you want a dev container, it will build prod,
# and from there add dependecies inside this container.
##################################################################################

#
# Stage PROD - minimal env
# build command: docker build --target prod -t <image_name> .
#

FROM ruby:2.6.6 as prod

# Define workdir

WORKDIR /home/docker-user/app

# Copy files
COPY . /home/docker-user/app

# Create base user

RUN useradd docker-user \
 && chown -R docker-user:docker-user /home/docker-user

# Install debian dependencies

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
 && apt-get -y --no-install-recommends install \
      locales \
      libsqlite3-dev \
      nodejs \
      cron \
      imagemagick \
 && rm -rf /var/lib/apt/lists/*

# Setup scheduler
# https://github.com/aptible/supercronic

ENV SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.11/supercronic-linux-amd64 \
    SUPERCRONIC=supercronic-linux-amd64 \
    SUPERCRONIC_SHA1SUM=a2e2d47078a8dafc5949491e5ea7267cc721d67c

RUN curl -fsSLO "$SUPERCRONIC_URL" \
 && echo "${SUPERCRONIC_SHA1SUM}  ${SUPERCRONIC}" | sha1sum -c - \
 && chmod +x "$SUPERCRONIC" \
 && mv "$SUPERCRONIC" "/usr/local/bin/${SUPERCRONIC}" \
 && ln -s "/usr/local/bin/${SUPERCRONIC}" /usr/local/bin/supercronic

# Setup locales

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# Run all future commands with this user

USER docker-user

# Setup gem config, install bundler, foreman and all Gemfile dependencies

RUN echo gem: --no-document > ~/.gemrc \
 && gem install 'bundler:~>2' foreman

RUN bundle install

#
# Stage DEV (default if you do docker built -t .) - we add all the dev dependencies here
# build command: docker build --target dev -t <image_name> .
#

FROM prod as dev

# Become root again so we can install all the dependecies we want

USER root

# Install npm resources

#RUN curl -L https://npmjs.org/install.sh | sh

# FIXME: do we really need this? all the time? takes 2mins to build out of the 4 mins (lib is out of date)

# Install psql. See bin/docker/psql

RUN apt-get update \
 && apt-get -y --no-install-recommends install \
      postgresql-client \
 && rm -rf /var/lib/apt/lists/*

# Install ruby spy

RUN \
  repo=https://github.com/rbspy/rbspy; \
  tag=$(curl -sLI -o /dev/null -w %{url_effective} $repo/releases/latest | cut -d/ -f8); \
  tar=$repo/releases/download/$tag/rbspy-x86_64-unknown-linux-gnu.tar.gz; \
  curl -sL $tar | tar xzC /usr/local/bin

# Run all future commands with this user

USER docker-user
