FROM centos:centos6

ENV RUBY_DIR /ruby/
ENV RUBY_VERSION 2.2.2
ENV RUBY_INSTALL $RUBY_DIR/$RUBY_VERSION

RUN rpm -Uvh \
    http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm && \
    yum update -y && \
    yum install -y which wget tar git nodejs \
    gcc patch readline-devel zlib-devel      \
    libyaml-devel libffi-devel openssl-devel \
    gdbm-devel ncurses-devel libxml-devel

RUN mkdir $RUBY_DIR && \
    cd $RUBY_DIR    && \
    git clone https://github.com/sstephenson/ruby-build.git && \
    $RUBY_DIR/ruby-build/install.sh                         && \
    cd $RUBY_DIR/ruby-build && ./bin/ruby-build $RUBY_VERSION $RUBY_INSTALL && \
    rm -rf $RUBY_DIR/ruby-build

ENV PATH $RUBY_INSTALL/bin:$PATH