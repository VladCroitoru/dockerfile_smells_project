FROM ruby:latest
MAINTAINER Dieter Provoost <dieter.provoost@marlon.be>

RUN apt-get update

RUN gem install capistrano -v 2.15.5
RUN gem install capistrano-ext

RUN apt-get clean -y
