FROM ruby:alpine
MAINTAINER Michon van Dooren <michon1992@gmail.com>

# Nokogiri dependencies
RUN apk add --update --no-cache \
  build-base \
  libxml2-dev \
  libxslt-dev

# Although the flag shouldn't be strictly necessary, it saves build time
RUN bundle config build.nokogiri --use-system-libraries

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD Gemfile .
ADD Gemfile.lock .
RUN bundle install --frozen
ADD trashclear.rb .

CMD ["ruby", "trashclear.rb"]
