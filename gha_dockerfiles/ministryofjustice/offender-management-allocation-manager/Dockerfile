FROM ruby:2.6.8-slim-bullseye

RUN \
  set -ex \
  && apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install \
    -y \
    --no-install-recommends \
    locales \
  && sed -i -e 's/# en_GB.UTF-8 UTF-8/en_GB.UTF-8 UTF-8/' /etc/locale.gen \
  && dpkg-reconfigure --frontend=noninteractive locales \
  && update-locale LANG=en_GB.UTF-8 \
  && apt-get clean

ENV \
  LANG=en_GB.UTF-8 \
  LANGUAGE=en_GB.UTF-8 \
  LC_ALL=en_GB.UTF-8

ARG VERSION_NUMBER
ARG COMMIT_ID
ARG BUILD_DATE
ARG BUILD_TAG

ENV APPVERSION=${VERSION_NUMBER}
ENV APP_GIT_COMMIT=${COMMIT_ID}
ENV APP_BUILD_DATE=${BUILD_DATE}
ENV APP_BUILD_TAG=${BUILD_TAG}

WORKDIR /app

RUN \
  set -ex \
  && apt-get update && apt-get install \
    -y \
    --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    libjemalloc-dev \
  && timedatectl set-timezone Europe/London || true \
  && gem update bundler --no-document \
  && apt-get clean

# Install Node.js and Yarn
RUN (curl -fsSL https://deb.nodesource.com/setup_16.x | bash -) \
    && apt-get install -y nodejs \
    && npm --global install yarn \
    && apt-get clean

# Install Ruby and Node dependencies
COPY Gemfile Gemfile.lock package.json ./
RUN yarn install \
    && bundle config set --local without 'development test' \
    && bundle install --jobs 2 --retry 3

COPY . /app

RUN mkdir -p /home/appuser && \
  useradd appuser -u 1001 --user-group --home /home/appuser && \
  chown -R appuser:appuser /app && \
  chown -R appuser:appuser /home/appuser

USER 1001

RUN RAILS_ENV=production rails assets:precompile
