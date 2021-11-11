FROM ruby:2.4.2
RUN mkdir /ms-events-and-places
WORKDIR /ms-events-and-places
ADD Gemfile /ms-events-and-places/Gemfile
ADD Gemfile.lock /ms-events-and-places/Gemfile.lock
RUN bundle install
ADD . /ms-events-and-places
