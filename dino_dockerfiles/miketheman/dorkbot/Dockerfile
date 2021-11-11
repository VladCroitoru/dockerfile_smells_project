FROM litaio/ruby:latest
MAINTAINER Mike Fiedler <miketheman@gmail.com>

WORKDIR /tmp
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock
RUN gem install bundler --no-rdoc --no-ri && bundle install

ADD . /code
WORKDIR /code

ENTRYPOINT ["bundle", "exec", "lita", "start"]
