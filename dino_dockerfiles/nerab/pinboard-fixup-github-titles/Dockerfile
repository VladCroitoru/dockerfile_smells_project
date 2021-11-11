FROM ruby:alpine

RUN apk add --no-cache                         \
      build-base                               \
      git                                      \
  && rm -rf /var/cache/apk/*                   \
  && rm -rf /usr/local/lib/ruby/gems/*/cache/* \
  && rm -rf ~/.gem

RUN mkdir /app
WORKDIR /app
ADD . /app
RUN gem install bundler --no-document
RUN bundle config --global silence_root_warning 1
RUN bundle config set --local without 'development test'
RUN bundle install --jobs 4

CMD bundle exec exe/pinboard-fixup-github-titles
