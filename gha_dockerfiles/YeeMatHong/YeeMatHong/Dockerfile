FROM ruby:2.7.0-alpine

ARG DATABASE_URL
ARG REDIS_URL
ARG SECRET_KEY_BASE
ARG RAILS_MASTER_KEY

ENV RAILS_ENV=production
ENV DATABASE_URL=$DATABASE_URL
ENV REDIS_URL=$REDIS_URL
ENV SECRET_KEY_BASE=$SECRET_KEY_BASE
ENV RAILS_MASTER_KEY=$RAILS_MASTER_KEY

RUN mkdir /app
WORKDIR /app

COPY Gemfile /app/
COPY Gemfile.lock /app/

RUN apk add --no-cache build-base gcc g++ postgresql-dev cargo linux-headers libffi-dev openssl-dev git tzdata libsodium-dev
RUN apk add --update nodejs npm

# Gemfile.lock requirement
RUN gem install bundler -v 2.1.4
RUN npm install -g yarn

RUN bundle install

COPY . /app/

RUN yarn install --check-files

RUN bundle exec rake webpacker:install
RUN bundle exec rake assets:precompile

EXPOSE 8000

CMD ["bundle", "exec", "rails", "s", "-b", "0.0.0.0", "-p", "8000"]
