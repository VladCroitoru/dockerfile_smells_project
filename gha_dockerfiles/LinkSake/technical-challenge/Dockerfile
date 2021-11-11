FROM ruby:3.0.2-slim AS backend-builder
ENV RAILS_ENV production
ENV NODE_ENV development
WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential git libpq-dev nodejs npm --no-install-recommends && apt-get clean && npm install -g yarn

COPY backend/Gemfile backend/Gemfile.lock /usr/src/app/
ARG BUNDLE_RUBYGEMS__PKG__GITHUB__COM
RUN bundle config set deployment 'true' && bundle install

FROM ruby:3.0.2-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV RAILS_ENV production
ENV RAILS_SERVE_STATIC_FILES true
ENV RAILS_LOG_TO_STDOUT true

RUN apt-get update && apt-get upgrade -y && apt-get install -y postgresql-client git curl --no-install-recommends && apt-get clean

COPY backend/Gemfile backend/Gemfile.lock /usr/src/app/
COPY --from=backend-builder /usr/src/app/vendor/bundle /usr/src/app/vendor/bundle
RUN bundle config set deployment 'true' && bundle install
COPY backend/. /usr/src/app/

EXPOSE 3000
RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN bundle exec rails --version
ENTRYPOINT [ "/usr/src/app/bin/bundle" ]
CMD ["exec", "rails", "server", "-b", "0.0.0.0"]