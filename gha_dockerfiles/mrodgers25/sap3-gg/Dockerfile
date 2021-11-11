FROM phusion/passenger-ruby27

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update -qq && apt-get install -y build-essential nodejs npm yarn imagemagick libsasl2-dev libpq-dev postgresql-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

SHELL [ "/bin/bash", "-l", "-c" ]

ENV APP_HOME /app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

RUN gem install bundler:1.17.3

ADD Gemfile Gemfile.lock package.json yarn.lock ./
RUN bundle check || bundle install
RUN yarn install

COPY . $APP_HOME

RUN chmod +x ./ops/entrypoint.sh

ENTRYPOINT ["/bin/bash", "./ops/entrypoint.sh"]
