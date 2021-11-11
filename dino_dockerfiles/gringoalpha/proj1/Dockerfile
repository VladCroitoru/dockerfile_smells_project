FROM ubuntu:14.04
MAINTAINER GPYPEC
RUN apt-get update && apt-get install -y ruby ruby-dev
RUN apt-get install -y wget
RUN wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
RUN dpkg -i puppetlabs-release-trusty.deb
RUN apt-get install -y puppet

RUN sudo apt-get install -y puppet-lint


