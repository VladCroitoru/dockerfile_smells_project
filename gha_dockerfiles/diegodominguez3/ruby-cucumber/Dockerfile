FROM ruby:3.0

# throw errors if Gemfile has been modified since Gemfile.lock
RUN bundle config --global frozen 1
COPY ./ /ruby-test
WORKDIR /ruby-test

RUN bundle install

CMD [ "bundle", "exec", "rake"]
