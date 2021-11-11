FROM quay.io/assemblyline/ruby:2.1.6

WORKDIR /usr/src/sidekicks

# Install Ruby Deps
COPY Gemfile /usr/src/sidekicks/
COPY Gemfile.lock /usr/src/sidekicks/
RUN bundle install

COPY . /usr/src/sidekicks

# Run the unit tests
RUN bundle exec rake

ENTRYPOINT ["/usr/src/sidekicks/bin/sidekick"]
