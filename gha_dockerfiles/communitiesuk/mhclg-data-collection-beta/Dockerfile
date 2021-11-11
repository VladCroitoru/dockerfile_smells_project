# Build compilation image
FROM ruby:3.0.2-alpine as builder

# The application runs from /app
WORKDIR /app

# Add the timezone as it's not configured by default in Alpine
RUN apk add --update --no-cache tzdata && \
  cp /usr/share/zoneinfo/Europe/London /etc/localtime && \
  echo "Europe/London" > /etc/timezone

# build-base: complication tools for bundle
# yarn: node package manager
# postgresql-dev: postgres driver and libraries
RUN apk add --no-cache build-base yarn postgresql-dev

# Install bundler to run bundle exec
# This should be the same version as the Gemfile.lock
RUN gem install bundler:2.2.3 --no-document

# Install gems defined in Gemfile
COPY .ruby-version Gemfile Gemfile.lock /app/

RUN bundle config set without "development test"
ARG BUNDLE_FLAGS="--jobs=4 --no-binstubs --no-cache"
RUN bundle install ${BUNDLE_FLAGS}

# Install node packages defined in package.json, including webpack
COPY package.json yarn.lock /app/
RUN yarn install --frozen-lockfile

# Copy all files to /app (except what is defined in .dockerignore)
COPY . /app/

# Compile assets and run webpack. We set a dummy secret key.
RUN RAILS_ENV=production bundle exec rails SECRET_KEY_BASE=pickasecuretoken assets:precompile

# Cleanup to save space in the production image
RUN rm -rf node_modules log tmp && \
      rm -rf /usr/local/bundle/cache && \
      rm -rf .env && \
      find /usr/local/bundle/gems -name "*.c" -delete && \
      find /usr/local/bundle/gems -name "*.h" -delete && \
      find /usr/local/bundle/gems -name "*.o" -delete && \
      find /usr/local/bundle/gems -name "*.html" -delete

# Build runtime image
FROM ruby:3.0.2-alpine as production

# The application runs from /app
WORKDIR /app

# Add postgres driver library
# Add the timezone as it's not configured by default in Alpine
RUN apk add --update --no-cache libpq tzdata && \
  cp /usr/share/zoneinfo/Europe/London /etc/localtime && \
  echo "Europe/London" > /etc/timezone

# Copy files generated in the builder image
COPY --from=builder /app /app
COPY --from=builder /usr/local/bundle/ /usr/local/bundle/

ARG GIT_COMMIT_SHA="UNKNOWN"
ENV GIT_COMMIT_SHA=${GIT_COMMIT_SHA}
RUN echo ${GIT_COMMIT_SHA} > ./GIT_COMMIT_SHA

ENV PORT=8080

EXPOSE ${PORT}

CMD RAILS_ENV=${RAILS_ENV} bundle exec rake db:migrate && bundle exec rails s -e ${RAILS_ENV} -p ${PORT} --binding=0.0.0.0
