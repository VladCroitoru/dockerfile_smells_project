FROM ruby:2.6.3
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs
RUN gem install bundler:2.0.2
RUN mkdir /coffee-shop
WORKDIR /coffee-shop
COPY Gemfile /coffee-shop/Gemfile
COPY Gemfile.lock /coffee-shop/Gemfile.lock
RUN bundle install
COPY . /coffee-shop

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# Start the main process.
CMD ["rails", "server", "-b", "0.0.0.0"]