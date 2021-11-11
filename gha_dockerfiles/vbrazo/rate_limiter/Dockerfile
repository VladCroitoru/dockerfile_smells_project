FROM ruby:2.7.2

WORKDIR /var/gem

COPY . .

RUN gem install bundler:1.17.2

RUN bundle check > /dev/null 2>&1 || bundle install -j4
