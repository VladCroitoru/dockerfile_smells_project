FROM ubuntu:16.04
MAINTAINER MJ "tywf91@gmail.com"

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk nginx autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev git curl

RUN git clone https://github.com/rbenv/rbenv /usr/local/rbenv
RUN mkdir -p /usr/local/rbenv/plugins
ENV RBENV_ROOT /usr/local/rbenv
ENV PATH $RBENV_ROOT/shims:$RBENV_ROOT/bin:$PATH

RUN git clone https://github.com/rbenv/ruby-build /usr/local/rbenv/plugins/ruby-build
RUN rbenv install jruby-9.1.2.0
RUN rbenv global jruby-9.1.2.0
RUN gem install bundler --no-ri --no-rdoc
RUN rbenv rehash