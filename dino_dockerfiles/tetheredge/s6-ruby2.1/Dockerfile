# VERSION 1.0.0
FROM jprjr/ubuntu-base:14.04
MAINTAINER Taylor Etheredge <taylor.etheredge@gmail.com>

RUN apt-get update
RUN apt-get upgrade -y

# Add Brightbox repository for Ruby package
RUN apt-get install -y software-properties-common && \
apt-add-repository ppa:brightbox/ruby-ng && \
apt-get update

# Install Ruby 2.1 package
RUN apt-get install -y ruby2.1 ruby2.1-dev
# Install bundler without the documenation and add gemrc file
RUN /bin/bash -l -c "gem install bundler --no-rdoc --no-ri && \
echo 'gem: --no-ri --no-rdoc' > ~/.gemrc"

# Remove unecessary files
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
