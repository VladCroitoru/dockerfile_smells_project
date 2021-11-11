FROM ubuntu:xenial

ENV DEBIAN_FRONTEND=noninteractive LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 LANGUAGE=en_US.UTF-8 GOPATH=$PWD PATH=$PATH:/opt/puppetlabs/bin

# Get things up to date
RUN apt-get update && apt-get -y dist-upgrade && locale-gen "en_US.UTF-8"
RUN apt-get -y install unzip tar software-properties-common wget curl ruby ruby-dev build-essential git

# Install dependencies
RUN add-apt-repository -y ppa:ubuntu-lxc/lxd-stable && \
    wget https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb && \
    dpkg -i puppetlabs-release-pc1-xenial.deb && \
    rm puppetlabs-release-pc1-xenial.deb && \
    curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
    apt-get update

ADD Gemfile .

# Install tooling
RUN apt-get -y install puppet-agent golang nodejs default-jdk maven && \
    curl -sSf https://sh.rustup.rs | sh -s -- -y && \
    apt-get clean && \
    gem install --no-rdoc --no-ri bundler && \
    bundle install --binstubs=/usr/local/bin

RUN puppet --version && \
	librarian-puppet version && \
	puppet-lint --version && \
	fpm-cook --version
