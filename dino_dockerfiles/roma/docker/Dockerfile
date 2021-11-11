FROM ruby:2.1.5

MAINTAINER Rui Bando <bando.rui@gmail.com>

ENV TC_VERSION=1.4.48
ENV TC_RUBY_VERSION=1.31.a
ENV ROMA_VERSION=1.1.0
ENV ROMA_CLIENT_VERSION=0.4.2
ENV ROMA_WORK_DIR=/opt/roma
ENV WORK_DIR=/usr/local/src

# Install library
RUN apt-get install -y gcc build-essential make zlib1g-dev libbz2-dev

# Install library
RUN cd /usr/local/src/ \
  && wget http://www.sqlite.org/2013/sqlite-autoconf-3080002.tar.gz \
  && tar xvfpz sqlite-autoconf-3080002.tar.gz \
  && cd sqlite-autoconf-3080002 \
  && ./configure \
  && make \
  && exit

# Install TokyoCabinet
RUN cd $WORK_DIR \
  && wget http://fallabs.com/tokyocabinet/tokyocabinet-$TC_VERSION.tar.gz \
  && tar -zxvf tokyocabinet-$TC_VERSION.tar.gz \
  && cd tokyocabinet-${TC_VERSION} \
  && ./configure --prefix=${ROMA_WORK_DIR}/libexec \
  && make \
  && make install

# Install TokyoCabinet Ruby
RUN cd $WORK_DIR \
  && wget https://github.com/roma/tokyocabinet-ruby/archive/v$TC_RUBY_VERSION.tar.gz \
  && tar -zxvf v$TC_RUBY_VERSION.tar.gz \
  && cd tokyocabinet-ruby-$TC_RUBY_VERSION \
  && gem build tokyocabinet.gemspec \
  && gem install --local tokyocabinet-$TC_RUBY_VERSION.gem -- --with-tokyocabinet-dir=${ROMA_WORK_DIR}/libexec
	
# Install required gems
RUN gem install eventmachine sqlite3 gdbm ffi rroonga

# Install ROMA
RUN cd $WORK_DIR \
  && wget https://github.com/roma/roma/archive/v$ROMA_VERSION.tar.gz \
  && tar -xvzf v$ROMA_VERSION.tar.gz \
  && mv roma-$ROMA_VERSION $ROMA_WORK_DIR

# Inatall ROMA Client
RUN cd $WORK_DIR \
  && wget https://github.com/roma/roma-ruby-client/archive/v$ROMA_CLIENT_VERSION.tar.gz \
  && tar xvfpz v$ROMA_CLIENT_VERSION.tar.gz \
  && mv -i roma-ruby-client-$ROMA_CLIENT_VERSION $ROMA_WORK_DIR/roma-ruby-client
