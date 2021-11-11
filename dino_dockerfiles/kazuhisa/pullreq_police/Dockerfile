FROM ruby:2.7.2
LABEL maintainer "Kazuhisa Yamamoto <ak.hisashi@gmail.com>"
RUN mkdir /work
WORKDIR /work
COPY Gemfile .
COPY Gemfile.lock .
COPY pullreq.rb .
RUN bundle install
CMD bundle exec ruby pullreq.rb