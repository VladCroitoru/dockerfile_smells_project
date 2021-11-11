FROM ruby:3.0

MAINTAINER Dmitriy.Rotatii "kvazilife@gmail.com"
ENV S3_KEY ""
ENV S3_PRIVATE_KEY ""
ENV PALLADIUM_TOKEN ""
ENV DOCUMENTSERVER_JWT ""
RUN mkdir -pv ~/.s3 && \
    echo $S3_KEY > ~/.s3/key && \
    echo $S3_PRIVATE_KEY > ~/.s3/private_key

RUN mkdir ~/.documentserver
RUN echo $DOCUMENTSERVER_JWT > ~/.documentserver/documentserver_jwt

RUN mkdir ~/.palladium
RUN echo $PALLADIUM_TOKEN > ~/.palladium/token

RUN mkdir /convert_service_testing
WORKDIR /convert_service_testing
ADD . /convert_service_testing
RUN gem install bundler
RUN bundle config set without 'test development'
RUN bundle install
