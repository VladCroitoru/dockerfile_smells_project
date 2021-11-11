FROM ruby:2.4.7-alpine3.10

RUN apk add \
  python3 \
  python3-dev \
  nodejs \
  yarn \
  alpine-sdk

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN bundle install

COPY package.json /usr/src/app/
COPY yarn.lock /usr/src/app/
RUN yarn

COPY . /usr/src/app

CMD bundle exec rake jobs:work
