FROM ruby:2.5-alpine
MAINTAINER Marnen Laibow-Koser <marnen@marnen.org>

# Install build tools and packages needed for native extensions
RUN apk add --update build-base postgresql-dev
# Install JS runtime. TODO: do we want to use therubyracer instead?
RUN apk add nodejs
# See https://github.com/phusion/passenger-docker/issues/195
RUN apk add tzdata
RUN apk add yarn

RUN gem install bundler

ARG workdir=/contraq

WORKDIR ${workdir}
COPY Gemfile Gemfile.lock ${workdir}/
RUN bundle install
COPY package.json yarn.lock ${workdir}/
RUN yarn install --verbose

COPY . ${workdir}

ARG port=3000

EXPOSE ${port}
ENV BUNDLE_GEMFILE Gemfile
ENV PORT ${port}

ENTRYPOINT ["bundle", "exec"]
CMD ["rails", "server", "-b", "0.0.0.0"]
