FROM  ruby:2.2
MAINTAINER  Steven Berlanga<zabawaba99@gmail.com>

ENV AGE_DAYS=0

ADD . cleaner/
WORKDIR cleaner
RUN bundle install

CMD bundle exec ruby cleaner.rb
