FROM ruby:2.4.2

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash

RUN apt-get update -yqq \
  && apt-get install -yqq --no-install-recommends \
  postgresql-client \
  nodejs

RUN npm install --global yarn

WORKDIR /usr/src/app
COPY Gemfile* ./
COPY package.json yarn.lock ./
RUN bundle install
RUN yarn install
COPY . .

# For a compile assets
ENV RAILS_ENV=production
ENV SECRET_KEY_BASE=xxxxxxxxx

ENV RAILS_LOG_TO_STDOUT=true
RUN rake assets:precompile
RUN mkdir -p tmp/pids

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["puma", "-C", "config/puma.rb", "-p", "3000"]