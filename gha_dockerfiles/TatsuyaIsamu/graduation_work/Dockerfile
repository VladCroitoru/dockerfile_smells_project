FROM ruby:2.6.5

RUN curl https://deb.nodesource.com/setup_12.x | bash
RUN wget --quiet -O - /tmp/pubkey.gpg https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo 'deb http://dl.yarnpkg.com/debian/ stable main' > /etc/apt/sources.list.d/yarn.list

RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y postgresql-client --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs vim yarn

RUN mkdir /graduation_work
WORKDIR /graduation_work

COPY Gemfile /graduation_work/Gemfile
COPY Gemfile.lock /graduation_work/Gemfile.lock

RUN gem install bundler
RUN bundle install

COPY . /graduation_work

COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

RUN mkdir -p tmp/sockets

RUN mkdir -p tmp/pids
