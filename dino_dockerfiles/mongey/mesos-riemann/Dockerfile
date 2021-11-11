FROM ruby:2.4

WORKDIR /tmp
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock
RUN bundle install

WORKDIR /app
COPY . /app/
CMD ["/app/run_app.rb"]
