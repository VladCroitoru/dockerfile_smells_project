FROM       centos:7
MAINTAINER Yosuke Yamamoto "yosuke@pyrites.jp"

## Setting Args
ARG RUBY_VERSION=2.3.3
ARG RUBY_BUILD_PATH=/usr/local/ruby-build
ARG RUBY_PATH=/opt/ruby

## Setting Environmet
ENV PATH $RUBY_PATH/bin:${PATH}

## Required Packages Install
RUN yum update -y && \
    yum install epel-release -y && \
    yum install bzip2 gcc make automake autoconfig readline-devel zlib-devel openssl-devel libffi-devel -y && \
    yum install git -y && \
    yum clean all

## Install ruby-build && ruby
RUN git clone https://github.com/rbenv/ruby-build.git $RUBY_BUILD_PATH  && \
    $RUBY_BUILD_PATH/install.sh && rm -Rf RUBY_BUILD_PATH && \
    mkdir -p $RUBY_PATH && ruby-build $RUBY_VERSION $RUBY_PATH && \
    gem install bundler

