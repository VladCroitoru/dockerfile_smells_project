FROM ubuntu:16.04
MAINTAINER bellbind

WORKDIR /tmp
RUN apt update
RUN apt upgrade -y
RUN apt install -y build-essential ruby-build autoconf subversion bison
RUN apt install -y libyaml-dev libncurses5-dev libffi-dev libgdbm-dev
RUN apt install -y pkg-config mecab mecab-ipadic-utf8 libmecab-dev wget sqlite3

ENV PATH /root/.rbenv/shims:$PATH
RUN rbenv install 1.8.7-p375
RUN rbenv local 1.8.7-p375
RUN rbenv rehash

RUN gem install rake -v 0.8.7 --no-ri --no-rdoc
RUN gem install rdoc -v 2.4.3 --no-ri --no-rdoc
RUN gem install mongrel --no-ri --no-rdoc
RUN gem install sqlite3 --no-ri --no-rdoc
RUN gem install rails -v 2.3.18 --no-ri --no-rdoc
RUN rbenv rehash

RUN wget http://mecab.googlecode.com/files/mecab-ruby-0.994.tar.gz
RUN tar xf mecab-ruby-0.994.tar.gz
WORKDIR /tmp/mecab-ruby-0.994
RUN gem build mecab-ruby.gemspec
RUN gem install mecab-ruby --no-ri --no-rdoc

WORKDIR /root
RUN rbenv local 1.8.7-p375
RUN rbenv rehash
RUN rm -rf /tmp/mecab-ruby-0.994
CMD bash
