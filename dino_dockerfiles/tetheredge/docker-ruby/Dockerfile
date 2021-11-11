FROM ubuntu:latest
MAINTAINER Taylor Etheredge <taylor.etheredge@gmail.com>
# VERSION 0.0.2

# Ignore the APT warnings about not having a TTY
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install -y build-essential libcurl3-gnutls curl git

# Add Brightbox repository for Ruby package
RUN apt-get install -y software-properties-common && \
	apt-add-repository ppa:brightbox/ruby-ng && \
	apt-get update

# Install Ruby 2.1 package
RUN apt-get install -y ruby2.1 ruby2.1-dev

# Install bundler without the documenation and add gemrc file
RUN /bin/bash -l -c "gem install bundler --no-rdoc --no-ri && \
	echo 'gem: --no-ri --no-rdoc' > ~/.gemrc"

# Clean up APT and remove temporary files
RUN apt-get clean -qq && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
