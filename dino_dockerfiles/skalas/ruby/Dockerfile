FROM ubuntu:14.04
MAINTAINER Miguel Escalante <miguel@opi.la>
RUN apt-get update && apt-get install -y build-essential wget  python-dev autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev git libpq-dev  && locale-gen es_MX.UTF-8 
## Ruby installation (2.1.2)  
RUN wget --no-verbose http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz -O /tmp/ruby-2.1.2.tar.gz && \
tar -xzf /tmp/ruby-2.1.2.tar.gz -C /tmp/ && \
cd /tmp/ruby-2.1.2/ && \
./configure --disable-install-doc && \
make && \
make install && \
rm -rf /tmp/* 
RUN gem install bundler
EXPOSE 80
