# Redis Trib for CentOS 7
# Version latest

FROM centos:7
MAINTAINER RiverYang "comicme_yanghe@icloud.com"

RUN yum update -y

RUN yum install -y wget gcc make zlib zlib-devel openssl openssl-devel readline-devel gdbm-devel

RUN cd /usr/local/src && \
wget http://download.redis.io/releases/redis-3.2.4.tar.gz && \
tar -zxvf redis-3.2.4.tar.gz && \
cd redis-3.2.4 && \
cp src/redis-trib.rb /usr/local/bin && \
cd .. && rm -rf redis*

RUN cd /usr/local/src && \
wget http://cache.ruby-lang.org/pub/ruby/2.3/ruby-2.3.1.tar.gz && \
tar -zxvf ruby-2.3.1.tar.gz && \
cd ruby-2.3.1 && ./configure --with-openssl-dir=/usr/bin && make && make install && \
cd ext/zlib && ruby ./extconf.rb --with-zlib-include=/usr/include --with-zlib-lib=/usr/lib  && make && make install && \
ruby -v && cd /usr/local/src && rm -rf ruby-2.3.1*

RUN gem install redis && gem list --local | grep redis

COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
