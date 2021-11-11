FROM ubuntu:16.04

MAINTAINER Dale <dale@daleslab.com>

RUN apt update \
&& apt install -y wget git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev

# Libraries for ruby
RUN apt-get update \
    && apt-get -y install \
        autoconf \
        bison \
        build-essential \
        curl \
        libffi-dev \
        libgdbm3 \
        libgdbm-dev \
        libmysqlclient-dev \
        libncurses5-dev \
        libreadline-dev \
        libssl-dev \
        libyaml-dev \
        zlib1g-dev \
        software-properties-common \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
    && apt-get -y install software-properties-common \
    && add-apt-repository -y ppa:brightbox/ruby-ng \
    && apt-get update \
    && apt-get -y install \
        ruby2.4 \
        ruby2.4-dev \
    && rm -rf /var/lib/apt/lists/*

RUN echo 'gem: --no-document' > /usr/local/etc/gemrc \
    && gem update \
    && gem install bundler
