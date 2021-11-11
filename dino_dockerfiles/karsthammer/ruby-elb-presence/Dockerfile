FROM ubuntu:14.04

RUN apt-get update && apt-get install -y ruby && gem install bundler --no-ri --no-rdoc

ADD Gemfile Gemfile.lock /app/
WORKDIR /app
RUN bundle install --deployment

ADD elb-presence.rb /app/elb-presence.rb
CMD /usr/bin/env ruby /app/elb-presence.rb
