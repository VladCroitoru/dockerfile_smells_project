FROM ubuntu:12.10
MAINTAINER henteko<henteko07@gmail.com>

# ruby install 
RUN apt-get update
RUN apt-get install -y wget build-essential libssl-dev zlib1g-dev
RUN apt-get install -y libreadline6 libreadline6-dev
WORKDIR /tmp/
RUN wget http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.0-preview1.tar.gz
RUN tar zxvf ruby-2.1.0-preview1.tar.gz
WORKDIR /tmp/ruby-2.1.0-preview1
RUN ./configure && make && make install
RUN gem install rubygems-update --no-ri --no-rdoc
RUN update_rubygems
RUN gem install bundler --no-ri --no-rdoc
