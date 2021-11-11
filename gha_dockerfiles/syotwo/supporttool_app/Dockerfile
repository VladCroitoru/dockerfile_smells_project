FROM ruby:2.7.1
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs yarn


WORKDIR /supporttool-app
COPY Gemfile /supporttool-app/Gemfile
COPY Gemfile.lock /supporttool-app/Gemfile.lock
RUN gem install bundler
RUN bundle install
COPY . /supporttool-app

RUN yarn install --check-files
RUN bundle exec rails webpacker:compile

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

CMD ["rails", "server", "-b", "0.0.0.0"]

