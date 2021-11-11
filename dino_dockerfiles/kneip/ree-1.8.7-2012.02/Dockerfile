# Ruby Enterprise Edition 1.8.7-2012.02
#
# VERSION       1.0

# ~~~~ Image base ~~~~
FROM phusion/baseimage:0.9.9
MAINTAINER zedtux, zedtux@zedroot.org


# ~~~~ OS Maintenance ~~~~
# Keep up-to-date the container OS
# and install dependencies for Ruby compilation
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      build-essential \
      wget \
      curl \
      git \
      zlib1g-dev \
      libssl-dev \
      libreadline-dev \
      libyaml-dev \
      libxml2-dev \
      libxslt-dev

RUN cd /usr/src && \
  wget http://rubyenterpriseedition.googlecode.com/files/ruby-enterprise-1.8.7-2012.02.tar.gz && \
  tar xzf ruby-enterprise-1.8.7-2012.02.tar.gz && \
  cd /usr/src/ruby-enterprise-1.8.7-2012.02/source && \
  wget 'https://github.com/wayneeseguin/rvm/raw/master/patches/ree/1.8.7/tcmalloc.patch' && \
  patch -p1 < tcmalloc.patch && \
  wget 'https://github.com/wayneeseguin/rvm/raw/master/patches/ree/1.8.7/stdout-rouge-fix.patch' && \
  patch -p1 < stdout-rouge-fix.patch && \
  wget 'https://github.com/wayneeseguin/rvm/raw/master/patches/ree/1.8.7/no_sslv2.diff' && \
  patch -p1 < no_sslv2.diff ; \
  wget 'https://github.com/wayneeseguin/rvm/raw/master/patches/ruby/ssl_no_ec2m.patch' && \
  patch -p1 < ssl_no_ec2m.patch && \
  wget 'https://github.com/wayneeseguin/rvm/raw/master/patches/ree/1.8.7/p358-p374.patch' && \
  patch -p1 < p358-p374.patch ; \
  wget 'https://github.com/wayneeseguin/rvm/raw/master/patches/ruby/GH-488.patch' && \
  patch -p1 < GH-488.patch && \
  cd .. && \
  ./installer --auto /usr/local --dont-install-useful-gems && \
  echo "RUBY_HEAP_MIN_SLOTS=600000\nRUBY_HEAP_SLOTS_INCREMENT=10000\nRUBY_HEAP_SLOTS_GROWTH_FACTOR=1.8\nRUBY_GC_MALLOC_LIMIT=59000000\nRUBY_HEAP_FREE_MIN=100000" >> /etc/environment
