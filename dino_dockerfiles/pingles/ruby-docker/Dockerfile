FROM ubuntu:14.04.1

RUN apt-get update
RUN apt-get -y install ca-certificates build-essential zlib1g-dev libssl-dev libreadline6-dev libyaml-dev

WORKDIR /tmp
ADD http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.5.tar.gz /tmp/ruby-2.1.5.tar.gz
RUN tar xvf ruby-2.1.5.tar.gz
WORKDIR /tmp/ruby-2.1.5
RUN ./configure
RUN make
RUN sudo make install

RUN sudo gem install bundler