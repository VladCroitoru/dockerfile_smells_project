FROM continuumio/miniconda

MAINTAINER Kozo Nishida <knishida@riken.jp>

RUN apt install -y ruby ruby-dev make libtool autoconf g++
RUN ln -s /usr/bin/libtoolize /usr/bin/libtool # See https://github.com/zeromq/libzmq/issues/1385

RUN gem install rbczmq iruby pry && ldconfig /var/lib/gems/2.1.0/gems/rbczmq-1.7.9/ext/rbczmq/dst/lib
RUN /opt/conda/bin/conda install jupyter -y && mkdir /opt/notebooks && iruby register
