FROM ruby:2.2.2-slim

ENV ROOT /apps/contract-hunt

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

RUN mkdir -p $ROOT
WORKDIR $ROOT

ADD Gemfile Gemfile.lock $ROOT/
ADD vendor $ROOT/vendor

#RUN bundle install --without development --deployment
RUN bundle install --local

VOLUME ["/data"]

ADD . $ROOT

CMD ["./bin/contract-hunt.sh"]
