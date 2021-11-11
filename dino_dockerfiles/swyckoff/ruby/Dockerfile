FROM ruby:2.1.5

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1

RUN mkdir -p /var/www
WORKDIR /var/www

ONBUILD COPY Gemfile /var/www/
ONBUILD COPY Gemfile.lock /var/www/
ONBUILD RUN bundle install

ONBUILD COPY . /var/www
