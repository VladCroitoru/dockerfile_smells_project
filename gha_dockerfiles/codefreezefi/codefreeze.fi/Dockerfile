FROM ruby:2.6-buster

ENV LANG C.UTF-8
RUN gem install bundler

ADD Gemfile Gemfile.lock /project/
WORKDIR /project
RUN bundle install

EXPOSE 4000
CMD bundle exec jekyll serve --destination /_site --watch --force_polling --host 0.0.0.0 --port 4000
