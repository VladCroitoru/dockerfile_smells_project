FROM centos:6

MAINTAINER Masashi Kurita <marty.marron@gmail.com>

RUN yum -y update
RUN yum -y install wget gcc git tar openssl openssl-devel bzip2 libffi-devel readline-devel

RUN wget http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.1.tar.gz
RUN tar xvzf ruby-2.1.1.tar.gz
RUN cd ruby-2.1.1 \
    && ./configure --prefix=/usr \
    && make \
    && make install

# Install RubyGems
RUN wget http://production.cf.rubygems.org/rubygems/rubygems-1.8.25.tgz
RUN tar xvzf rubygems-1.8.25.tgz
RUN cd rubygems-1.8.25 \
    && ruby setup.rb config \
    && ruby setup.rb setup \
    && ruby setup.rb install

# install bundler
RUN gem install bundler
