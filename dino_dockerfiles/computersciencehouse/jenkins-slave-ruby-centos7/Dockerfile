FROM openshift/jenkins-slave-base-centos7

MAINTAINER Steven Mirabito <smirabito@csh.rit.edu>

ENV LC_ALL=en_US.UTF-8 \
    RUBY_VERSION=2.4.2 \
    NODEJS_VERSION=6.11.5 \
    NPM_CONFIG_PREFIX=$HOME/.npm-global \
    PATH=$HOME/node_modules/.bin/:$HOME/.npm-global/bin/:$PATH \
    BUNDLE_PATH=$HOME/.bundle

# Install Ruby
RUN INSTALL_PKGS="autoconf automake bison bzip2 gcc-c++ libffi-devel libtool readline-devel sqlite-devel zlib-devel glibc-headers glibc-devel libyaml-devel openssl-devel" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y && \
    cd /usr/src && \
    wget https://cache.ruby-lang.org/pub/ruby/${RUBY_VERSION::-2}/ruby-${RUBY_VERSION}.tar.gz && \
    tar -zxf ruby-${RUBY_VERSION}.tar.gz && \
    cd ruby-${RUBY_VERSION} && \
    ./configure && \
    make && \
    make install && \
    cd / && \
    rm -rf /usr/src/ruby* && \
    gem install bundler

# Install NodeJS
RUN rpm -i https://rpm.nodesource.com/pub_6.x/el/7/x86_64/nodesource-release-el7-1.noarch.rpm && \
    INSTALL_PKGS="nodejs" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    ln -s /usr/lib/node_modules/nodemon/bin/nodemon.js /usr/bin/nodemon && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y

RUN chown -R 1001:0 $HOME && \
    chmod -R g+rw $HOME

USER 1001
