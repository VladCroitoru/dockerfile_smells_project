FROM ruby:2.1
RUN bundle config --global frozen 1
RUN mkdir -p /usr/src/app && mkdir -p /baha && mkdir -p /workspace
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN bundle install && bundle exec rake install
COPY docker-entrypoint.sh /entrypoint.sh
WORKDIR /baha
ENTRYPOINT ["/bin/bash","/entrypoint.sh"]
