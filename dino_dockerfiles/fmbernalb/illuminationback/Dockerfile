FROM ruby:2.4

RUN mkdir /illuminationSA_Backend
WORKDIR /illuminationSA_Backend

ADD Gemfile /illuminationSA_Backend/Gemfile
ADD Gemfile.lock /illuminationSA_Backend/Gemfile.lock

RUN bundle install
ADD . /illuminationSA_Backend
