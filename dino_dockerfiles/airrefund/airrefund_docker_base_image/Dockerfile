FROM ruby:2.2.2
MAINTAINER ryanfox1985 <wolf.fox1985@gmail.com>

# Update and upgrade
RUN apt-get -q update && apt-get -qy upgrade
RUN apt-get install apt-transport-https

RUN echo "deb https://apt.dockerproject.org/repo debian-jessie main" >> /etc/apt/sources.list.d/docker.list
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

# Note the new setup script name for Node.js v0.12
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -

# Install packages
RUN apt-get install -qy build-essential python-dev docker-engine nodejs curl build-essential libpq-dev imagemagick ghostscript
RUN gem install bundler

RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py
RUN pip install awscli

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
