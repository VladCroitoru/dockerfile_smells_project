FROM ruby:3.0.2

WORKDIR /neuronet-rb
RUN gem install bundler -v 2.2.25

COPY Gemfile Gemfile.lock ./
RUN bundle install

COPY . ./
ENTRYPOINT ["./entrypoints/docker-entrypoint.sh"]