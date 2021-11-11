FROM ruby:2.2

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN bundle install
ENTRYPOINT ["/usr/src/app/worker.rb"]

