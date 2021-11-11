FROM ruby:alpine3.6

LABEL author="Seosamh Cahill"

WORKDIR /app

COPY Gemfile Gemfile.lock ./

RUN \
  apk --update add --no-cache \
  build-base \
  && gem install bundler \
  && bundle install \
  && apk del build-base

COPY . .

ENV RACK_ENV=development

EXPOSE 9292

CMD [ "rackup" ]