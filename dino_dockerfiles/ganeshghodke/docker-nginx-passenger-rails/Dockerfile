
# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Ganesh Ghodke

# Setup all needed dependencies
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install build-essential libssl-dev libyaml-dev libreadline-dev openssl wget curl git-core zlib1g-dev bison libxml2-dev libxslt1-dev libcurl4-openssl-dev nodejs libsqlite3-dev sqlite3

# Install rvm and ruby
ENV RUBY_VERSION 2.2.1
ENV RAILS_VERSION 4.2.1

RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN \curl -sSL https://get.rvm.io | bash -s stable --rails
RUN echo 'source /usr/local/rvm/scripts/rvm' >> /etc/bash.bashrc
RUN /bin/bash -l -c 'rvm requirements'
RUN /bin/bash -l -c 'rvm install $RUBY_VERSION && rvm use $RUBY_VERSION --default'
RUN /bin/bash -l -c 'rvm rubygems current'

# Install nginx and passenger
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7
RUN echo "deb https://oss-binaries.phusionpassenger.com/apt/passenger trusty main" > /etc/apt/sources.list.d/passenger.list
RUN cat /etc/apt/sources.list.d/passenger.list
RUN chown root: /etc/apt/sources.list.d/passenger.list
RUN chmod 600 /etc/apt/sources.list.d/passenger.list
RUN apt-get install apt-transport-https
RUN apt-get update
RUN apt-get -y install nginx-extras passenger

# Install bundler and rails
RUN gem install bundler
RUN /bin/bash -l -c 'gem install bundler'
RUN /bin/bash -l -c 'gem install rails --version=$RAILS_VERSION'

# Expose ports
EXPOSE 80

# Set the default command to execute
# when creating a new container
#CMD ["service", "nginx", "start"]
