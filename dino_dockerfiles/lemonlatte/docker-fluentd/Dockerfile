FROM ubuntu:14.04

MAINTAINER Jim Yeh <lemonlatte@gmail.com>

RUN apt-get update

RUN apt-get -yqq install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev

RUN curl -o ruby.tgz http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.0.tar.gz
RUN mkdir /ruby
RUN tar -xzvf ruby.tgz -C /ruby --strip-components=1
WORKDIR ruby/
RUN ./configure
RUN make
RUN make install

WORKDIR /
RUN gem install fluentd --no-ri --no-rdoc

ADD setup.sh /

ENTRYPOINT ["fluentd"]
