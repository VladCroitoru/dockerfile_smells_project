# This Dockerfile is intended to build a production-ready Docker container with
# the app... however, further shrinking can be achieved...
# See - for example - https://blog.jtlebi.fr/2015/04/25/how-i-shrunk-a-docker-image-by-98-8-featuring-fanotify
FROM ruby:2.2.5-slim
MAINTAINER Roberto Quintanilla <vov@icalialabs.com>

ENV PATH=/usr/src/app/bin:$PATH RAILS_ENV=production
WORKDIR /usr/src/app

# 1: Install dependencies:

# 1.1: Copy just the Gemfile & Gemfile.lock, to avoid the build cache failing
# whenever any other file changed and installing dependencies all over again - a
# must if your'e developing this Dockerfile...
ADD ./Gemfile* /usr/src/app/

# 1.2: Install dependencies (including nodejs, nginx and supervisord):
RUN set -ex \
  && apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
  && echo "deb http://nginx.org/packages/debian/ jessie nginx" > /etc/apt/sources.list.d/nginx.list \
  && apt-get update \
  && runDeps=' \
      ca-certificates \
      gettext-base \
      libpq5 \
      nginx=1.10.1-1~jessie \
      supervisor \
  ' \
  && buildDeps=' \
      autoconf \
      g++ \
      gcc \
      git \
      libpq-dev \
      libxml2-dev \
      libxslt-dev \
      make \
      patch \
  ' \
  && apt-get install -y --no-install-recommends $runDeps $buildDeps \
  && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/nginx.list \
  && bundle install --deployment --without development test \
  && apt-get purge -y --auto-remove $buildDeps \
  && ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

# 2: Add the application code:

# 2.1: Copy the rest of the code, and then compile the assets:
ADD . /usr/src/app
RUN set -ex \
  && mkdir -p /usr/src/app/tmp/cache \
  && mkdir -p /usr/src/app/tmp/pids \
  && mkdir -p /usr/src/app/tmp/sockets \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done \
  && apt-get update \
  && buildDeps='git xz-utils curl' \
  && apt-get install -y --no-install-recommends $buildDeps \
  && rm -rf /var/lib/apt/lists/* \
  && export NPM_CONFIG_LOGLEVEL=info \
  && export NODE_VERSION=6.3.1 \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && npm install -g bower \
  && DATABASE_URL=postgres://postgres@example.com:5432/fakedb \
  TWITTER_API_KEY=SOME_KEY TWITTER_API_SECRET=SOME_SECRET \
  SECRET_KEY_BASE=10167c7f7654ed02b3557b05b88ece \
  rake assets:precompile \
  && apt-get purge -y --auto-remove $buildDeps \
  && for asset in $(ls /usr/src/app/tmp/ember-cli/apps/frontend/assets); do \
    ln -s "/usr/src/app/tmp/ember-cli/apps/frontend/assets/${asset}" "/usr/src/app/public/assets/${asset}"; \
  done \
  && chown -R nobody /usr/src/app

# 3: Expose the following ports:
# - Port 3000 for the Rails web process
EXPOSE 3000

# 4: Set the user used to run the process to a 'nobody' unprivileged user:
USER nobody

# 5: Set the default Puma config values:
ENV MIN_THREADS=8 RAILS_MAX_THREADS=12 PUMA_WORKR_COUNT=2

# 6: Set the default command:
CMD bundle exec puma --bind tcp://0.0.0.0:3000
