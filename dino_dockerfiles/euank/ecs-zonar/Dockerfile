FROM ruby:2

# Public Domain
MAINTAINER Euan Kemp <euank@euank.com>

RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY Gemfile Gemfile.lock add_route53_entries.rb UNLICENSE ./
COPY lib ./lib
RUN bundle install --without development test

# Poor man's crontab
CMD ["sh", "-c", "while true; do ruby add_route53_entries.rb || exit 10; sleep 30; done"]
