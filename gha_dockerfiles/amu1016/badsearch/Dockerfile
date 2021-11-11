FROM ruby:2.6.5

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs libmariadb-dev vim

RUN mkdir /badsearch

WORKDIR /badsearch

ADD Gemfile /badsearch/Gemfile
ADD Gemfile.lock /badsearch/Gemfile.lock

RUN gem install bundler
RUN bundle install

ADD . /badsearch

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 80

RUN mkdir -p tmp/sockets
RUN mkdir -p tmp/pids

CMD ["rails", "server", "-b", "0.0.0.0"]