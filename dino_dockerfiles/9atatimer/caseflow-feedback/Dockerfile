FROM ruby:2.3.3
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs libaio1 unzip

RUN mkdir /caseflow-feedback
WORKDIR /caseflow-feedback
ADD Gemfile /caseflow-feedback/Gemfile
ADD Gemfile.lock /caseflow-feedback/Gemfile.lock
RUN bundle install
ADD . /caseflow-feedback
