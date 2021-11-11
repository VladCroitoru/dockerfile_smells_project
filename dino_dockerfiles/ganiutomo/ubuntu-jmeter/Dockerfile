#
# Gani Utomo Ubuntu Dockerfile
#
# https://github.com/ganiutomo/ubuntu-jmeter
#

# Pull base image.
FROM ubuntu:14.04

MAINTAINER Gani Utomo <ganiutomo@gmail.com>

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get -qq update && \
  apt-get -y -qq upgrade && \
  apt-get -y -qq install openjdk-7-jre-headless wget && \
  rm -rf /var/lib/apt/lists/* && \
  wget -q http://archive.apache.org/dist/jmeter/binaries/apache-jmeter-2.11.tgz && \
  tar -xzf apache-jmeter-2.11.tgz && \
  rm apache-jmeter-2.11.tgz && \
  mv apache-jmeter-2.11 /usr/local/jmeter

ENV PATH /usr/local/jmeter/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

EXPOSE 1099 4445
