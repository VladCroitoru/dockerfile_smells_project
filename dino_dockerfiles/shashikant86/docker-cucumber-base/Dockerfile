FROM centos:centos6
MAINTAINER Shashikant Jagtap <shashikant.jagtap@aol.co.uk>

RUN yum -y update && yum -y groupinstall 'Development Tools' && yum -y install \
    kernel-devel \
    bzip2-devel \
    libcurl \
    libcurl-devel \
    openssl-devel \
    libevent-devel \
    libffi-devel \
    glib2-devel \
    libjpeg-devel \
    openssl \
    openssl-devel \
    libxml2-devel \
    libxslt-devel \
    zlib-devel \
    wget \
    && yum clean all

RUN rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6 \
    && rpm -Kih http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm \
    && yum -y install libyaml-devel \
    && yum clean all

RUN yum -y update && yum install -y \
    bzr \
    mercurial \
    && yum clean all

RUN yum -y update && yum install -y \
    tar \
    && yum clean all


ENV PHANTOM_JS_TAG 2.0.0

RUN yum install -y fontconfig freetype freetype-devel fontconfig-devel libstdc++

RUN mkdir -p /opt/phantomjs

RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2

RUN tar -xjvf phantomjs-1.9.8-linux-x86_64.tar.bz2 --strip-components 1 

RUN ln -s bin/phantomjs /usr/bin/phantomjs


ENV RUBY_MAJOR 1.9
ENV RUBY_VERSION 1.9.3-p550

RUN yum -y update && yum -y install ruby && yum clean all \
    && mkdir -p /usr/src/ruby \
    && curl -SL "http://cache.ruby-lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.bz2" | tar -xjC /usr/src/ruby --strip-components=1 \
    && cd /usr/src/ruby \
    && autoconf \
    && ./configure --disable-install-doc \
    && make \
    && yum remove -y ruby \
    && make install \
    && rm -r /usr/src/ruby


RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"

ENV GEM_HOME /usr/local/bundle
ENV PATH $GEM_HOME/bin:$PATH
RUN gem install bundler \
	&& bundle config --global path "$GEM_HOME" \
	&& bundle config --global bin "$GEM_HOME/bin"

ENV BUNDLE_APP_CONFIG $GEM_HOME  

RUN yum install -y gcc-c++ patch readline readline-devel zlib zlib-devel 
RUN yum install -y libyaml-devel libffi-devel openssl-devel make 
RUN yum install -y bzip2 autoconf automake libtool bison iconv-devel
RUN yum install -y which tar

RUN curl -sSL https://rvm.io/mpapis.asc | gpg --import -
RUN curl -L get.rvm.io | bash -s stable

RUN source /etc/profile.d/rvm.sh
RUN /bin/bash -l -c "rvm requirements"
RUN /bin/bash -l -c "rvm install 2.2"
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"
