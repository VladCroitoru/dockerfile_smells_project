FROM ruby:2.3
COPY Gemfile Gemfile
COPY app app
RUN bundle install
CMD bundle exec ruby app/sync.rb
