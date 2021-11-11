FROM ruby:2.2.5

WORKDIR /app

ADD Gemfile /app/
ADD Gemfile.lock /app/
RUN bundle install --jobs 3 --deployment --without development test

ADD . /app

ENV PORT 80
ENV BIND 0.0.0.0

EXPOSE 80
