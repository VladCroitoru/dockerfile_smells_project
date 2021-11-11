FROM ruby:2.7.1
RUN apt-get update -qq && apt-get install -y nodejs postgresql-client

RUN gem install bundler -v 2.1.4

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn

WORKDIR /smartflix
COPY . /smartflix

RUN bundle check || bundle install
RUN yarn install --check-files

CMD ["rails", "server", "-b", "0.0.0.0"]
