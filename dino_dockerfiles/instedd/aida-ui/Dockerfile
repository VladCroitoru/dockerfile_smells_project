FROM ruby:2.4.2

RUN \
  apt-get update && \
  # node
  curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
  apt-get install -y nodejs build-essential libpq-dev && \
  # yarn
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
  apt-get update && apt-get install -y yarn && \
  # clean
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /app
WORKDIR /app
ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock
RUN bundle install
ADD package.json /app/package.json
ADD yarn.lock /app/yarn.lock
RUN yarn install

ADD . /app

RUN if [ -d .git ]; then git describe --always > VERSION; fi

RUN bundle exec rake assets:precompile RAILS_ENV=production SECRET_KEY_BASE=secret SETTINGS__BASE_URL=http://test.host/

ENV RAILS_ENV production
ENV RAILS_SERVE_STATIC_FILES true
ENV RAILS_LOG_TO_STDOUT true
ENV PORT 80

EXPOSE $PORT

CMD bundle exec rails s -p $PORT -b '0.0.0.0'
