FROM phusion/baseimage:0.9.12

# Set correct environment variables.
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

###
### Added ruby 2.0
###
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 914D5813 
RUN echo "deb http://ppa.launchpad.net/gds/govuk/ubuntu precise main" > /etc/apt/sources.list.d/gds-govuk-precise.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D88E42B4
RUN echo 'deb http://packages.elasticsearch.org/logstash/1.4/debian stable main' > /etc/apt/sources.list.d/logstash.list
RUN apt-get update -qq

# Ensure the bash is the latest version
RUN apt-get install --only-upgrade bash

# We need netcat-traditional if we want to generate a metric from the command line
# The default netcat hangs when UDP transport is specified
RUN apt-get install -y  openjdk-7-jre-headless
RUN apt-get install -y --force-yes statsd netcat-traditional logstash

# Fix broken path to so that 'env node' works again
RUN ln -s /usr/bin/nodejs /usr/bin/node

# Ensure logstash user is member of adm group so it can read logs in /var/log
RUN usermod -a -G adm logstash

# install service files for runit
ADD logstash.service /etc/service/logstash/run
ADD statsd.service /etc/service/statsd/run
RUN chmod +x /etc/service/logstash/run
RUN chmod +x /etc/service/statsd/run

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
