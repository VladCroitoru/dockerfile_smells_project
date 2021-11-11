FROM ubuntu:xenial

MAINTAINER Mike Clarke <michaelclarkecs@gmail.com>

RUN apt-get update && \
    apt-get install -y wget

RUN wget https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb && \
    dpkg -i puppetlabs-release-pc1-xenial.deb && \
    apt-get update

RUN apt-get install -y puppetserver

ADD puppetserver-defaults /etc/default/puppetserver

VOLUME /etc/puppetlabs/code
VOLUME /opt/puppetlabs/puppet/ssl

EXPOSE 8140

ENTRYPOINT ["/opt/puppetlabs/server/bin/puppetserver", "foreground"]
