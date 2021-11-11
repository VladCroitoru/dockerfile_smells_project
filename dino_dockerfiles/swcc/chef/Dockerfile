# Docker container with chef-solo & berkshelf
FROM ubuntu:latest
MAINTAINER Paul B. "paul+swcc@bonaud.fr"

RUN apt-get -y update

# Install Chef
RUN apt-get -y install curl build-essential libxml2-dev libxslt-dev git wget lsb-release
RUN curl -L https://www.opscode.com/chef/install.sh | bash
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc

# Install Berkshelf with chef's own ruby
# And install gecode from binaries (compilation fails when installed by the gem)
RUN echo "deb http://apt.opscode.com/ `lsb_release -cs`-0.10 main" | tee /etc/apt/sources.list.d/opscode.list
RUN mkdir -p /etc/apt/trusted.gpg.d
RUN gpg --keyserver keys.gnupg.net --recv-keys 83EF826A
RUN gpg --export packages@opscode.com | tee /etc/apt/trusted.gpg.d/opscode-keyring.gpg > /dev/null
RUN apt-get -y update
RUN apt-get install -y opscode-keyring # permanent upgradeable keyring
RUN apt-get upgrade -y
RUN apt-get install -y libgecode-dev
RUN USE_SYSTEM_GECODE=1 /opt/chef/embedded/bin/gem install berkshelf

# Cleanup
RUN apt-get autoremove
RUN apt-get clean
