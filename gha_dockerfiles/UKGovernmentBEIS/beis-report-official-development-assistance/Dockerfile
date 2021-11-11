# ------------------------------------------------------------------------------
# base
# ------------------------------------------------------------------------------
FROM ruby:2.7.3 AS base
MAINTAINER dxw <rails@dxw.com>

RUN apt-get update && apt-get install -qq -y \
  build-essential \
  libpq-dev \
  --fix-missing --no-install-recommends

ENV APP_HOME /app
ENV DEPS_HOME /deps

ARG RAILS_ENV
ENV RAILS_ENV ${RAILS_ENV:-production}
ENV NODE_ENV ${RAILS_ENV:-production}

RUN echo "\nexport PATH=/usr/local/bin:\$PATH\n\n# Stop here if non-interactive shell\n[[ \$- == *i* ]] || return\n\ncd /app" >> ~/.bashrc

# ------------------------------------------------------------------------------
# dependencies
# ------------------------------------------------------------------------------
FROM base AS dependencies

# Set up install environment
RUN mkdir -p ${DEPS_HOME}
WORKDIR ${DEPS_HOME}
# End

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
  && apt-get install -y nodejs \
  && npm install --global yarn

# Install Ruby dependencies
COPY Gemfile ${DEPS_HOME}/Gemfile
COPY Gemfile.lock ${DEPS_HOME}/Gemfile.lock

RUN gem update --system 3.2.16
RUN gem update rake 13.0.1
RUN gem install bundler -v 2.1.4

RUN bundle config set frozen 'true'

# Configure bundler for the environment
RUN if [ ${RAILS_ENV} = "production" ]; then \
  bundle config set without 'development test'; \
  elif [ ${RAILS_ENV} = "test" ]; then \
  bundle config set without 'development'; \
  else \
  bundle config set without 'test'; \
  fi

RUN bundle config
RUN bundle install --retry 3 --jobs 4
# end

# Install JavaScript dependencies
COPY package.json ${DEPS_HOME}/package.json
COPY yarn.lock ${DEPS_HOME}/yarn.lock
RUN yarn install
#end

# ------------------------------------------------------------------------------
# web
# ------------------------------------------------------------------------------
FROM dependencies AS web

# Set up install environment
RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}
# end

COPY . ${APP_HOME}

# This must be ordered before rake assets:precompile
RUN cp -R $DEPS_HOME/node_modules $APP_HOME/node_modules
RUN cp -R $DEPS_HOME/node_modules/govuk-frontend/govuk/assets $APP_HOME/app/assets

RUN \
  RAILS_ENV=$RAILS_ENV \
  DOMAIN="stand-in.local" \
  SECRET_KEY_BASE="super secret" \
  DATABASE_URL="postgres://stand-in:5432" \
  REDIS_URL="redis://stand-in.local:6379" \
  AUTH0_CLIENT_ID="stand-in" \
  AUTH0_CLIENT_SECRET="stand-in" \
  AUTH0_DOMAIN="stand-in.local" \
  bundle exec rake assets:precompile --quiet

# create tmp/pids
RUN mkdir -p tmp/pids

ARG current_sha
ARG time_of_build

ENV CURRENT_SHA=$current_sha
ENV TIME_OF_BUILD=$time_of_build

# db setup
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 3000

CMD ["bundle", "exec", "puma"]

# ------------------------------------------------------------------------------
# test
# ------------------------------------------------------------------------------
FROM web as test

RUN apt-get install -qq -y firefox-esr \
  shellcheck

ARG gecko_driver_version=0.26.0

RUN wget https://github.com/mozilla/geckodriver/releases/download/v$gecko_driver_version/geckodriver-v$gecko_driver_version-linux64.tar.gz
RUN tar -xvzf  geckodriver-v$gecko_driver_version-linux64.tar.gz
RUN rm geckodriver-v$gecko_driver_version-linux64.tar.gz
RUN chmod +x geckodriver
RUN mv geckodriver* /usr/local/bin
