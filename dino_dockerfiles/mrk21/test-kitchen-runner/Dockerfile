FROM jpetazzo/dind:latest
MAINTAINER Yuichi Murata <mrk21info+docker@gmail.com>

# Base packages
RUN apt-get update
RUN apt-get install -y software-properties-common openssh-client git

# Ruby 2.2 with bundler
RUN add-apt-repository -y ppa:brightbox/ruby-ng
RUN apt-get update
RUN apt-get install -y ruby2.2
RUN gem install bundler

# Ansible latest version
RUN add-apt-repository -y ppa:ansible/ansible
RUN apt-get update
RUN apt-get install -y ansible
