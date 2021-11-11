FROM ruby:latest

# Install system dependencies
RUN apt-get update -qq && apt-get -qq install -y \
    curl ca-certificates bzip2 imagemagick jq libfontconfig \
    mysql-client xz-utils \
    --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

# Docker
# https://hub.docker.com/_/docker/

ENV DOCKER_CHANNEL stable
ENV DOCKER_VERSION 17.06.0-ce
# TODO ENV DOCKER_SHA256
# https://github.com/docker/docker-ce/blob/5b073ee2cf564edee5adca05eee574142f7627bb/components/packaging/static/hash_files !!
# (no SHA file artifacts on download.docker.com yet as of 2017-06-07 though)
ENV DOCKER_ARCH x86_64

RUN set -ex; \
    if ! curl -fL -o docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${DOCKER_ARCH}/docker-${DOCKER_VERSION}.tgz"; then \
      echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from '${DOCKER_CHANNEL}' for '${DOCKER_ARCH}'"; \
      exit 1; \
    fi; \
    tar --extract \
		  --file docker.tgz \
		  --strip-components 1 \
		  --directory /usr/local/bin/; \
    rm docker.tgz; \
    docker -v

# Node
# https://hub.docker.com/_/node/

ENV NPM_CONFIG_LOGLEVEL error
ENV NODE_VERSION 8.2.1

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

RUN npm set progress=false && \
    npm install -g --progress=false yarn && \
    npm cache clean --force

# Install phantomjs
ENV PHANTOMJS_VERSION 2.1.1

RUN curl -SLO "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2" \
    && mkdir "phantomjs-$PHANTOMJS_VERSION-linux-x86_64" \
    && tar -jxvf "phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2" -C "phantomjs-$PHANTOMJS_VERSION-linux-x86_64" --strip-components=1 \
    && mv "phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs" /usr/local/bin \
    && rm -rf "phantomjs-$PHANTOMJS_VERSION-linux-x86_64" "phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2"

RUN gem install bundler

# Bug with bundler 1.13
# See: https://github.com/bundler/bundler/issues/5005
RUN bundle config disable_exec_load true

# Use HTTPS instead of SSH
RUN bundle config github.https true

# Set Rails to run in production
ENV RAILS_ENV test
ENV RACK_ENV test
