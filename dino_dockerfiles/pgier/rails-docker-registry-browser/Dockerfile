
FROM ruby:2.3.3

ENV APP_DIR=/opt/rails-docker-registry-browser \
    REGISTRY_HOST_PORT="registry.foo.com:80"

WORKDIR $APP_DIR

RUN apt-get update -qq && apt-get install -y nodejs

RUN mkdir -p $APP_DIR

ADD Gemfile Gemfile.lock $APP_DIR/

RUN bundle install

ADD . $APP_DIR

CMD ["rails", "server", "--port", "3000", "--binding", "0.0.0.0"]
