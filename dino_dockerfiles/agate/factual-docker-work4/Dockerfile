FROM phusion/passenger-ruby23:latest

MAINTAINER agate<agate.hao@gmail.com>

RUN apt-get update
RUN apt-get install -y byobu vim-nox bash-completion sudo
RUN apt-get install -y libqt4-dev libqtwebkit-dev npm s3cmd

RUN curl -L https://toolbelt.treasuredata.com/sh/install-ubuntu-xenial-td-agent2.sh | sh
RUN td-agent-gem install fluent-plugin-s3

RUN npm install bower -g

RUN ssh-keygen -A

ADD bootstrap.sh /etc/my_init.d/099_bootstrap

ADD Gemfile /tmp/Gemfile
ADD Gemfile.lock /tmp/Gemfile.lock
RUN cd /tmp && bundle install

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
