FROM ubuntu:16.04

LABEL version 5.1.2-5

ENV DEBIAN_FRONTEND noninteractive

ENV PASSENGER_VERSION 5.1.2

RUN apt-get update && apt-get install -y software-properties-common curl && apt-get clean
RUN add-apt-repository -y ppa:brightbox/ruby-ng
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list
RUN apt-get update && \
    apt-get install -y build-essential \
                       apache2 apache2-dev \
                       ruby2.3 ruby2.3-dev \
                       libcurl4-openssl-dev \
                       libssl-dev \
                       libpcre3-dev \
                       libapr1-dev libaprutil1-dev \
                       git-core \
                       libpq-dev \
                       nodejs \
                       tzdata \
                       yarn \
                       supervisor && \
    apt-get clean
RUN gem install bundler --no-ri --no-rdoc
RUN gem install passenger --no-ri --no-rdoc --version "${PASSENGER_VERSION}"
RUN passenger-install-apache2-module --auto
