FROM ruby:2.4.1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock
RUN bundle install

COPY Procfile Procfile
COPY Rakefile Rakefile
COPY config.ru config.ru
COPY .standalone_migrations .standalone_migrations
COPY lib lib
COPY db db
COPY config config
COPY commands.rb commands.rb
COPY commands commands

CMD ["bundle", "exec", "foreman", "start"]
