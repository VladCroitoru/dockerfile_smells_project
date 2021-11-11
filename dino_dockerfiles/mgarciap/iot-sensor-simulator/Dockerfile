FROM ruby:2.2.0
MAINTAINER Manuel Garcia <manuel.garcia@altoros.com> / <mgarciap@gmail.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN bundle install --without test development

EXPOSE 9393
ENTRYPOINT ["rackup", "--port", "9393", "--host", "0.0.0.0"]
