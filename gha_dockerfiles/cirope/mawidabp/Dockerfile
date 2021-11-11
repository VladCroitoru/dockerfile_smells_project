ARG APP_HOME=/opt/app
ARG BUNDLE_BIN=$GEM_HOME/bin
ARG BUNDLE_GEMFILE=$APP_HOME/Gemfile
ARG PATH=$BUNDLE_BIN:$PATH
ARG RAILS_ENV=production

# ----------------------
# --- Assets builder ---
# ----------------------
FROM ruby:alpine AS builder

ARG APP_HOME
ARG BUNDLE_BIN
ARG BUNDLE_GEMFILE
ARG PATH
ARG RAILS_ENV

RUN apk add --update --no-cache \
  build-base                    \
  linux-headers                 \
  nodejs                        \
  postgresql-dev                \
  tzdata

RUN mkdir $APP_HOME

WORKDIR $APP_HOME

COPY Gemfile $APP_HOME/Gemfile
COPY Gemfile.lock $APP_HOME/Gemfile.lock

RUN gem update --system && gem update --force --no-document
RUN bundle config set deployment 'true' && bundle install

COPY . $APP_HOME
COPY config/application.yml.example $APP_HOME/config/application.yml

RUN bundle exec rails assets:precompile DB_ADAPTER=nulldb

# ----------------------
# --- Release image ----
# ----------------------
FROM ruby:alpine

ARG APP_HOME
ARG BUNDLE_BIN
ARG BUNDLE_GEMFILE
ARG PATH
ARG RAILS_ENV

ENV RAILS_LOG_TO_STDOUT true
ENV RAILS_SERVE_STATIC_FILES true

ENV HOME $APP_HOME
ENV USER nobody
ENV PORT 3000

RUN apk add --update --no-cache \
  imagemagick                   \
  nodejs                        \
  postgresql-dev                \
  tzdata

COPY --from=builder $APP_HOME $APP_HOME
COPY --from=builder $GEM_HOME $GEM_HOME

RUN chown -R $USER: $APP_HOME

WORKDIR $APP_HOME

USER $USER

EXPOSE $PORT

CMD [ "bundle", "exec", "rails", "server" ]
