FROM ruby:2.4
ENV TZ=Asia/Tokyo
ENV RUBYOPT=-EUTF-8
RUN apt-get update && apt-get install -y build-essential libpq-dev postgresql-client redis-server
RUN gem install rails 
RUN mkdir /install
WORKDIR /install

ADD Gemfile /install/Gemfile
ADD Gemfile.lock /install/Gemfile.lock

RUN bundle install

WORKDIR /app
CMD sleep infinity
