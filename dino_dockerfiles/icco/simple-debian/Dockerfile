FROM tianon/debian:wheezy
MAINTAINER Nat Welch <nat@natwelch.com>

# Install all of the packages
ENV DEBIAN_FRONTEND noninteractive
RUN echo 'deb http://gce_debian_mirror.storage.googleapis.com/ wheezy main contrib non-free' > /etc/apt/sources.list
RUN apt-key update
RUN apt-get update
ADD packages.txt /tmp/
RUN apt-get -qy install `cat /tmp/packages.txt`

# Configure Language Environment
RUN apt-get install -y locales
ADD locale.gen /etc/locale.gen
RUN locale-gen
RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install Ruby
RUN mkdir -p /opt/ruby && cd /opt/ruby && curl --progress ftp://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.3.tar.gz | tar xz
RUN cd /opt/ruby/ruby* && ./configure && make && make install
RUN echo "gem: --no-ri --no-rdoc" > /root/.gemrc
RUN gem install bundler

# Read an identity file
RUN echo " IdentityFile ~/.ssh/id_rsa" >> /etc/ssh/ssh_config

# Verify the correct host for Github
RUN mkdir -p /root/.ssh
RUN ssh-keyscan -t rsa,dsa github.com | sort -u > /root/.ssh/known_hosts
