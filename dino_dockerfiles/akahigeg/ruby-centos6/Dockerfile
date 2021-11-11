# Ruby on CentOS6
FROM centos:centos6
LABEL maintainer="akahigeg@gmail.com"

# install packages for Rails and more...
RUN yum -y update && yum -y install gcc gcc-c++ libxml2-devel libxslt-devel openssl-devel readline-devel mysql-devel wget git

# install Ruby and Bundler
ENV RUBY_MAJOR_VERSION 2.5
ENV RUBY_VERSION 2.5.1
ENV CONFIGURE_OPTS --disable-install-doc
RUN wget https://cache.ruby-lang.org/pub/ruby/$RUBY_MAJOR_VERSION/ruby-$RUBY_VERSION.tar.bz2
RUN tar jxf ruby-$RUBY_VERSION.tar.bz2
RUN cd ruby-$RUBY_VERSION && ./configure && make && make install
RUN gem install bundler

