FROM ruby:3.0.2-buster as development

RUN echo "Running Dockerfile with the environment: DEVELOPMENT"

RUN gem install bundler

EXPOSE 3000

WORKDIR /app

ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock
RUN bundle config set with ‘development’
RUN bundle install

ADD ./ /app

FROM development as production

ARG ENVIRONMENT
ARG SECRET_KEY_BASE

RUN echo "Running Dockerfile with the environment: PRODUCTION"

ENV RAILS_ENV production

CMD ["rails", "server", "-b", "0.0.0.0"]