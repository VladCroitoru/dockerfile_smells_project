FROM ubuntu:14.04

ENV RUBY_VERSION "2.4.0"

MAINTAINER Richard Hao "https://github.com/haoxilu"

RUN echo "2.4.0" > /VERSION

# == Ubuntu Mirror on 163 for China network
RUN \
    echo "deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y curl

# == Install Packages for Ruby Environments.
RUN curl -sSL https://raw.githubusercontent.com/haoxilu/init.d/2099f762d3b8a09293634b3c07b044d39d7b5b3c/install_packages | bash

# Clean apt-get
RUN \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# == Install Ruby
ENV RUBY_BUILD_MIRROR_URL=https://cache.ruby-china.org
RUN echo 'gem: --no-document' >> /usr/local/etc/gemrc &&\
    mkdir /src && cd /src && git clone https://github.com/rbenv/ruby-build.git --depth 1 &&\
    cd /src/ruby-build && ./install.sh &&\
    cd / && rm -rf /src/ruby-build &&\
    ruby-build $RUBY_VERSION /usr/local/
RUN gem update --system
RUN gem install bundler

# == Install Nginx
RUN curl -sSL https://git.io/vVHhf | bash

ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_PATH="$GEM_HOME" \
	BUNDLE_BIN="$GEM_HOME/bin" \
	BUNDLE_SILENCE_ROOT_WARNING=1 \
	BUNDLE_APP_CONFIG="$GEM_HOME"
ENV PATH $BUNDLE_BIN:$PATH
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \
	&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"
