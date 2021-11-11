FROM ruby:2.2.2
MAINTAINER mdouchement

RUN mkdir -p /usr/src/app
RUN mkdir -p /data/storage
RUN mkdir -p /data/db
WORKDIR /usr/src/app

ENV LANG C.UTF-8
ENV RAILS_ENV production
ENV RACK_ENV production
ENV DEVISE_SECRET_KEY tmp_376ea25aaa66984733a90920c263ba138e1e571aaf3a1a54cd2b819cb06e8b7fb311027b639eb8f55d8d53c27cf2df378ceb36008462057861d824bd13a0
ENV STORAGE_DIRECTORY /data/storage
ENV DATABASE_PATH /data/db/production.sqlite3

RUN mkdir -p tmp/pids
COPY . /usr/src/app
# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1
RUN bundle install --deployment --without development test

RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN bundle exec rake assets:precompile

VOLUME /data/storage
VOLUME /data/db
EXPOSE 3000
CMD bundle exec rake db:migrate && \
    SECRET_KEY_BASE=$(bundle exec rake secret) \
    DEVISE_SECRET_KEY=$(bundle exec rake secret) \
    bundle exec unicorn -p 3000 -c config/unicorn.rb
