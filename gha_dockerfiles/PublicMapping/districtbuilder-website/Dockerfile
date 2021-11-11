FROM ruby:2.6.2

RUN \
    apt-get update && apt-get install -y \
    nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN bundle config --global frozen 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN bundle install

ENTRYPOINT ["/usr/local/bin/bundle", "exec", "jekyll"]
