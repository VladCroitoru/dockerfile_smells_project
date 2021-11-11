FROM ruby:2.7
WORKDIR /opt/app
COPY Gemfile /opt/app/
COPY Gemfile.lock /opt/app/
RUN bundle install
CMD bundle exec jekyll build
