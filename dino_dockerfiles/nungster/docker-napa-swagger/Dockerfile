FROM ruby:2.3-alpine

MAINTAINER Nung Bedell <danungsta@gmail.com>

RUN apk add --update bash mysql-dev mysql-client curl jq vim openssl make \
        ruby-dev ruby-mysql2 build-base ca-certificates sqlite-dev git

#Ruby reqs
RUN apk add ruby ruby-bundler sqlite-libs ruby-io-console ruby-bigdecimal \
        ruby-rake libstdc++ py-pip ruby-dev make build-base libffi-dev \
        ruby-mysql2 sqlite-dev 

RUN mkdir /app

COPY files/app /app
COPY scripts/run.sh /run.sh

WORKDIR /app/api_server
RUN bundle install

EXPOSE 9292

#CMD "/run.sh"
CMD "bash"
