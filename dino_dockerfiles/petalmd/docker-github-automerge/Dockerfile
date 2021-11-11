FROM ruby:2.3.1-onbuild
MAINTAINER Francis Robichaud <frobichaud@petalmd.com>

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN bundle install

COPY . /app
CMD ["bundle", "exec", "ruby", "app.rb"]

EXPOSE 8080