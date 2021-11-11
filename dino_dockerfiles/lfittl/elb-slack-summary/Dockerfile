FROM ubuntu:xenial

RUN adduser --disabled-password --gecos "" app
ENV APPDIR /home/app/

# Install helpful packages & bundle dependencies
RUN apt-get update -qq && apt-get upgrade -y && apt-get install -y build-essential curl git wget

# Install Ruby
RUN curl https://s3-external-1.amazonaws.com/heroku-buildpack-ruby/cedar-14/ruby-2.2.4.tgz | tar -xzC /usr/local/ \
    && echo "gem: --no-document" >> /etc/gemrc \
    && gem install -q bundler

USER app
WORKDIR $APPDIR
COPY Gemfile Gemfile.lock $APPDIR
RUN bundle install --deployment --without development test

USER root
COPY . $APPDIR
RUN chown -R app:app $APPDIR

USER app
WORKDIR $APPDIR

USER root
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD su -c "bundle exec /home/app/main.rb" app
