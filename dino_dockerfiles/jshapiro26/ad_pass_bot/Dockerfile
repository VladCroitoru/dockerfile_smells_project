FROM ruby:2.3.1
MAINTAINER Jeremy Shapiro

WORKDIR /opt/ad_pass_bot/

ADD Gemfile .
ADD Gemfile.lock .
RUN bundle install

ADD ad_pass_bot.rb .

CMD ruby ad_pass_bot.rb 