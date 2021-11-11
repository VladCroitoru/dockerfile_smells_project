ARG RUBY_VERSION=3.0.2
FROM ruby:${RUBY_VERSION}-alpine

ENV RAILS_ENV=production
ENV NODE_ENV=production
ENV NOKOGIRI_USE_SYSTEM_LIBRARIES=1
ENV LANG C.UTF-8

WORKDIR /tmp

RUN echo @edge http://dl-cdn.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories && \
  echo @edge http://dl-cdn.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories && \
  apk add --no-cache \
  libxml2-dev \
  libxslt-dev \
  libstdc++@edge \
  libuv@edge \
  nodejs@edge \
  nodejs-npm@edge \
  yarn@edge \
  gmp-dev@edge \
  g++@edge \
  make@edge \
  postgresql-dev@edge \
  tzdata@edge

RUN gem install bundler
COPY ./Gemfile ./Gemfile.lock /tmp/
RUN bundle install -j 4 --without development test

COPY package.json yarn.lock /tmp/
RUN yarn install

COPY . /app
WORKDIR /app
RUN cp -a /tmp/node_modules /app

RUN SECRET_KEY_BASE=dummy_value bundle exec rake assets:precompile
RUN rm -rf node_modules

ENTRYPOINT ["bundle", "exec"]
CMD rails server -p $PORT
