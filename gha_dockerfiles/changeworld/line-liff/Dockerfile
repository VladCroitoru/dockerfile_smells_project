FROM ruby:2.6.6

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update -qq && apt-get install -y build-essential nodejs yarn postgresql-client

RUN mkdir -p /app
WORKDIR /app

COPY Gemfile Gemfile.lock ./

RUN gem update bundler
RUN bundle install
COPY . .

CMD ["rails", "server", "-b", "0.0.0.0"]
