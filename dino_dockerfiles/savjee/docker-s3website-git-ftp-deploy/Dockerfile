FROM ruby:2.7
MAINTAINER Xavier Decuyper <hi@savjee.be>

RUN gem install s3_website

RUN apt-get update -qy
RUN apt-get install -y openjdk-8-jre-headless
RUN mkdir repo

WORKDIR /repo
